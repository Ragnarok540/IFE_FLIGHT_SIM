from geographiclib.geodesic import Geodesic
import math
import time
from datetime import datetime, timedelta
from coordenada import Coordenada


class Simulador:
    """Simula un vuelo a una velocidad constante,
    en línea recta, entre dos coordenadas.
    """

    def __init__(self, origen, destino, velocidad=340.0):
        self.geod = Geodesic.WGS84
        self.origen = origen
        self.destino = destino
        self.velocidad = velocidad
        self.tiempo_inicio = datetime.fromtimestamp(time.time())
        self.ruta = {}

    def distancia(self):
        """Retorna la distancia en metros
        entre las coordenadas de origen y destino.
        """
        g = self.geod.Inverse(self.origen.latitud,
                              self.origen.longitud,
                              self.destino.latitud,
                              self.destino.longitud)
        distancia = g['s12']
        return distancia

    def tiempo(self):
        """Tiempo de vuelo en segundos, depende de
        la velocidad (por defecto 340 m/s, es decir
        la velocidad del sonido) y la distancia
        entre el origen y destino.
        """
        tiempo = self.distancia() / self.velocidad
        return tiempo

    def tiempo_fin(self):
        """Tiempo de finalización del vuelo."""
        tiempo = self.tiempo()
        tiempo_fin = self.tiempo_inicio + timedelta(seconds=tiempo)
        return tiempo_fin

    def calcular_ruta(self):
        """Calcula la ruta del vuelo."""
        l = self.geod.InverseLine(self.origen.latitud,
                                  self.origen.longitud,
                                  self.destino.latitud,
                                  self.destino.longitud)
        pasos = int(math.ceil(l.s13 / self.velocidad))

        for i in range(pasos + 1):
            s = min(self.velocidad * i, l.s13)
            g = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)
            self.ruta[i] = [g['lat2'], g['lon2']]

        return self.ruta

    def tiempo_transcurrido(self):
        """Tiempo transcurrido del vuelo."""
        tiempo_actual = datetime.fromtimestamp(time.time())
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
        return tiempo_transcurrido.total_seconds()

    def ubicacion_actual(self):
        """Ubicacion actual del avion."""
        tiempo = math.floor(self.tiempo_transcurrido())
        try:
            ubicacion = self.ruta[tiempo]
        except KeyError:
            return [0, 0] # None
        return self.ruta[tiempo]
