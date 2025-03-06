import unittest
from modelos.boa_constrictor import BoaConstrictor

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        "Crear una nueva boa en cada iteracion"
        self.boa = BoaConstrictor("Peters", 32.2, 3, "Cuba", 2)
        
    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")
        
    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 64.4)
        
    def test_alimentar(self):
        for _ in range(10):
            self.boa.comer_raton()
            
        with self.assertRaises(ValueError) as context:
            self.boa.comer_raton()
            
        self.assertEqual(str(context.exception), "Demasiados Ratones!")