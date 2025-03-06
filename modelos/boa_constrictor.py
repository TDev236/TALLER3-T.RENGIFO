from modelos.animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0
        

    def hacer_sonido(self):
        return "¡Tsss!"
    
    def comer_raton(self):
        if self._ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += 1
        
    def ratones_comidos(self):
        return self._ratones_comidos
