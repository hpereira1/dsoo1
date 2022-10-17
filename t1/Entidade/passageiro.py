from abc import ABC, abstractmethod
from pessoa import Pessoa


class Passageiro(Pessoa):
    def __init__(self, nome: str, id: int, email: str, historico_de_voos: dict):
        super().__init__(nome, id, email)
        self.__historico_de_voos = historico_de_voos
        
    @property
    def historico_de_voos(self):
        return self.__historico_de_voos
    
    @historico_de_voos.setter
    def historico_de_voos(self, historico_de_voos):
        if isinstance(historico_de_voos, dict):
            self.__historico_de_voos = historico_de_voos