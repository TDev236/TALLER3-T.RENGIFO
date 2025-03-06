from modelos.animal import Animal

class AnimalExotico(Animal):
    def __init__(self, nombre:str, peso:float,edad: int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self):
        return self._impuestos * self._peso
    
    def hacer_sonido(self): # Cada animal exotico tendra su propio sonido, pero en esta clase no se define
        pass
    
