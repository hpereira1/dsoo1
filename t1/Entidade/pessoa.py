from abc import ABC,abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, id: int, email: str):
        self.__nome = nome
        self.__id = id
        self.__email = email
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id
    
    @property
    def email(self):
        return self.__email
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id
    
    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email