import unittest # la libreria para la pruebas
from modelos.huron import Huron 

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Tavio", 30.2, 23, "Venezuela", 0.5)
    
    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "Eek Eek!")
        
    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 15.1)