from Entidade.pessoa import Pessoa
from abc import ABC,abstractmethod
from Entidade.cargo import Cargo

class Funcionario(Pessoa):
    def __init__(self, nome: str, id: str, email: str, cargo: Cargo):
        super().__init__(nome, id, email)    
        self.__cargo = Cargo
        
    @property
    def cargo(self):
        return self.__cargo
        
    @cargo.setter
    def cargo(self, cargo):
        if isinstance(cargo, Cargo):
            self.__cargo = cargo
