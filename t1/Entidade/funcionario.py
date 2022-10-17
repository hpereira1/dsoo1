from ast import Raise
from pessoa import Pessoa
from abc import ABC,abstractmethod
from t1.Entidade.cargo import Cargo

class Funcionario(Pessoa):
    def __init__(self, nome: str, id: int, email: str, cargo: Cargo):
        super().__init__(nome, id, email)    
        self.__cargo = Cargo
        
    @property
    def cargo(self):
        return self.__cargo
        
    @cargo.setter
    def cargo(self, cargo):
        if isinstance(cargo, Cargo):
            self.__cargo = cargo
