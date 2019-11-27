from geographiclib.geodesic import Geodesic
import math
import time
from random import uniform
from datetime import datetime, timedelta
from coordenada import Coordenada


class Simulador:
    """Simula un vuelo a una velocidad constante,
    en línea recta, entre dos coordenadas.
    """

    def __init__(self):
        self.geod = Geodesic.WGS84

    def definir_coordenadas(self, origen, destino):
        """Define las coordenadas de la simulación actual"""
        self.origen = origen
        self.destino = destino

    def definir_velocidad(self, mach):
        """Define la velocidad de la simulación actual
        en un múltiplo de la velocidad del sonido.
        """
        velocidad = 295.0
        self.velocidad = velocidad * mach

    def calc_distancia(self):
        """Retorna la distancia en metros
        entre las coordenadas de origen y destino.
        """
        g = self.geod.Inverse(self.origen.latitud,
                              self.origen.longitud,
                              self.destino.latitud,
                              self.destino.longitud)
        distancia = g['s12']
        self.distancia = distancia
        return distancia

    def calc_tiempo(self):
        """Tiempo de vuelo en segundos, depende de
        la velocidad (por defecto 295 m/s, es decir
        la velocidad del sonido) y la distancia
        entre el origen y destino.
        """
        tiempo = self.calc_distancia() / self.velocidad
        self.tiempo = tiempo
        return tiempo

    def calc_tiempo_fin(self):
        """Tiempo de finalización del vuelo."""
        tiempo = self.calc_tiempo()
        tiempo_fin = self.tiempo_inicio + timedelta(seconds=tiempo)
        self.tiempo_fin = tiempo_fin

    def calcular_ruta(self):
        """Calcula la ruta del vuelo."""
        self.ruta = { }
        l = self.geod.InverseLine(self.origen.latitud,
                                  self.origen.longitud,
                                  self.destino.latitud,
                                  self.destino.longitud)
        pasos = int(math.ceil(l.s13 / self.velocidad))

        for i in range(pasos + 1):
            s = min(self.velocidad * i, l.s13)
            g = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)
            self.ruta[i] = [g['lat2'], g['lon2']]

    def tiempo_transcurrido(self):
        """Tiempo transcurrido del vuelo en segundos."""
        tiempo_actual = datetime.fromtimestamp(time.time())
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
        return tiempo_transcurrido.total_seconds()

    def tiempo_restante(self):
        """Tiempo restante del vuelo en segundos."""
        tiempo_actual = datetime.fromtimestamp(time.time())
        tiempo_restante = self.tiempo_fin - tiempo_actual
        return tiempo_restante.total_seconds()

    def ubicacion_actual(self):
        """Ubicacion actual del avion."""
        tiempo = math.floor(self.tiempo_transcurrido())
        try:
            ubicacion = self.ruta[tiempo]
        except KeyError:
            return [999, 999]
        return ubicacion

    def iniciar_vuelo(self):
        """Inicia la simulación, llamar luego de
        definir las coordenadas de origen  destino.
        """
        self.tiempo_inicio = datetime.fromtimestamp(time.time())
        self.calcular_ruta()
        self.calc_tiempo_fin()

    def temperatura_interior(self):
        """Temperatura al interior del avión
        en grados Celsius.
        """
        return uniform(23.45, 23.55)

    def temperatura_exterior(self):
        """Temperatura en el exterior del avión
        en grados Celsius.
        """
        return uniform(-54.15, -54.05)

    def altitud(self):
        """Altitud del avión en metros."""
        return uniform(10666, 10670)

    def vel(self):
        """Velocidad del avión en metros por segundo."""
        return uniform(self.velocidad - 0.1, self.velocidad + 0.1)
