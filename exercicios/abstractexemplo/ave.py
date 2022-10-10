from animal import Animal
from abc import ABC,abstractmethod


class Ave(Animal):
    @abstractmethod
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo
    
    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo
    
    def produzir_som(self):
        return "AVE: PRODUZ SOM: PIU"
        
    def mover(self):
        return "ANIMAL: DESLOCOU " + str(self.tamanho_passo) + " VOANDO"
        
    