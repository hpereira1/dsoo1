import datetime
from Entidade.plano_de_voo import PlanoDeVoo


class Voo:
    def __init__(self, id:str, data: int):
        self.__id = id
        self.__data = data
    
    
 
    @property
    def id(self):
        return self.__id
    @property
    def data(self):
        return self.__data
   
    
    @id.setter
    def id(self,id):
        self.__id = id
   
    @data.setter
    def data (self,data):
        self.__data = data                    
        