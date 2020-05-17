import unittest
from simulador import Simulador
from coordenada import Coordenada

class SimuladorTestCase(unittest.TestCase):

    def setUp(self):
        self.sim = Simulador()
        self.origen = Coordenada(4.81267, -75.7395)
        self.destino = Coordenada(3.54322, -76.3816)
        self.maxDiff = None

    def test_definir_coordenadas(self):
        self.sim.definir_coordenadas(self.origen, self.destino)

        esperado = 4.81267
        observado = self.sim.origen.latitud
        self.assertEqual(esperado, observado)

        esperado = -76.3816
        observado = self.sim.destino.longitud
        self.assertEqual(esperado, observado)

    def test_definir_velocidad(self):
        self.sim.definir_velocidad(1)

        esperado = 295.0
        observado = self.sim.velocidad
        self.assertEqual(esperado, observado)

        self.sim.definir_velocidad(1000)

        esperado = 295000.0
        observado = self.sim.velocidad
        self.assertEqual(esperado, observado)

    def test_calc_distancia(self):
        self.sim.definir_coordenadas(self.origen, self.destino)

        esperado = 157440.23702528956
        observado = self.sim.calc_distancia()
        self.assertEqual(esperado, observado)

    def test_calc_tiempo(self):
        self.sim.definir_coordenadas(self.origen, self.destino)
        self.sim.definir_velocidad(1)

        esperado = 533.6957187297951
        observado = self.sim.calc_tiempo()
        self.assertEqual(esperado, observado)

    def test_calcular_ruta(self):
        self.sim.definir_coordenadas(self.origen, self.destino)
        self.sim.definir_velocidad(100)

        esperado = {0: [4.81267, -75.7395],
                    1: [4.574854328422334, -75.85997423623975],
                    2: [4.337016818381328, -75.98036900284852],
                    3: [4.099158620627947, -76.10068848953729],
                    4: [3.8612808835291523, -76.22093687700661],
                    5: [3.6233847532023256, -76.34111833745125],
                    6: [3.5432200000000003, -76.38160000000003]}
        self.sim.calcular_ruta()
        observado = self.sim.ruta
        self.assertEqual(esperado, observado)

    def test_temperatura_interior(self):
        esperado = 23.45
        observado = self.sim.temperatura_interior()
        self.assertLessEqual(esperado, observado)

        esperado = 23.55
        observado = self.sim.temperatura_interior()
        self.assertGreaterEqual(esperado, observado)

    def test_temperatura_exterior(self):
        esperado = -54.15
        observado = self.sim.temperatura_exterior()
        self.assertLessEqual(esperado, observado)

        esperado = -54.05
        observado = self.sim.temperatura_exterior()
        self.assertGreaterEqual(esperado, observado)

    def test_altitud(self):
        esperado = 10666
        observado = self.sim.altitud()
        self.assertLessEqual(esperado, observado)

        esperado = 10670
        observado = self.sim.altitud()
        self.assertGreaterEqual(esperado, observado)

    def test_vel(self):
        self.sim.definir_velocidad(1)

        esperado = self.sim.velocidad - 0.1
        observado = self.sim.vel()
        self.assertLessEqual(esperado, observado)

        esperado = self.sim.velocidad + 0.1
        observado = self.sim.vel()
        self.assertGreaterEqual(esperado, observado)
