from asyncio import protocols
import datetime
from Entidade.plano_de_voo import PlanoDeVoo


class Voo:
    def __init__(self, id:str, data: int, 
                 plano_voo:PlanoDeVoo = None 
                 ):
        self.__id = id
        self.__data = data
        self.__plano_voo = plano_voo
        self.__passageiros_voo = []
        self.__tripulantes_voo = []    
    
    @property
    def passageiros_voo(self):
        return self.__passageiros_voo
    @property
    def tripulantes_voo(self):
        return self.__tripulantes_voo
    @property
    def id(self):
        return self.__id
    @property
    def data(self):
        return self.__data
    @property
    def plano_voo(self):
        return self.__plano_voo
   
    
    @id.setter
    def id(self,id):
        self.__id = id
   
    @data.setter
    def data (self,data):
        self.__data = data
    @plano_voo.setter
    def plano_voo (self,plano_voo):
        self.__plano_voo = plano_voo         
    
    @passageiros_voo.setter
    def passageiros_voo(self, passageiros_voo):
        self.__passageiros_voo = passageiros_voo
    @tripulantes_voo.setter
    def tripulantes_voo(self, tripulantes_voo):
        self.tripulantes_voo = tripulantes_voo