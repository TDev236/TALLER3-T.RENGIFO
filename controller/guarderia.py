from modelos.boa_constrictor import BoaConstrictor
from modelos.huron import Huron

class Guarderia:
    def __init__(self):
        #aqui creamos dos boas y dos hurones
        self.boas = [
            BoaConstrictor("Pablo", 20, 5, "Brasil", 1.2),
            BoaConstrictor("Luis", 22, 6, "Colombia", 1.1)
        ]
        self.hurones = [
            Huron("Leo", 5, 3, "Argentina", 0.8),
            Huron("Pablinho", 4,2, "Mexico", 0.9)
        ]
        
    def alimentar_boa(self, boa):
        if boa is None:
            return "La Boa no existe"
        
        try:
            boa.comer_raton()
            return "Exito"
        except ValueError:
            return "La boa esta llena"