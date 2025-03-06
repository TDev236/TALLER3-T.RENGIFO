from abc import ABC, abstractmethod
from modelos.ianimal import IAnimal

class Animal(IAnimal, ABC):
    def __init__(self, nombre, peso, edad):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0
        
    def comer(self, kilos):
        self._kilos_comidos += kilos
    
    def obtener_kilos_comidos(self):
        return self._kilos_comidos
    
    @abstractmethod
    def hacer_sonido(self):
        return "Depende del animal"
   
