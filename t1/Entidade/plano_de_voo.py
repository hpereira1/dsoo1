from Entidade.aeronave import Aeronave

class PlanoDeVoo():
    
    def __init__(self, id_voo: str, codigo: str, distancia: float, numero_passageiros: int, peso: float, aeronave:Aeronave ):
        self.__id_voo = id_voo
        self.__codigo = codigo
        self.__distancia = distancia
        self.__numero_passageiros = numero_passageiros
        self.__peso = peso        
        self.__aeronave = aeronave
        
        
    ##Adicionar ao diagrama
    @property
    def id_voo(self):
        return self.__id_voo
    @property
    def codigo(self):
        return self.__codigo
    @property
    def distancia (self):
        return self.__distancia
    @property
    def numero_passageiros(self):
        return self.__numero_passageiros
    @property
    def peso(self):
        return self.__peso
    @property
    def aeronave(self):
        return self.__aeronave
    
    ##Adicionar ao diagrama
    @id_voo.setter
    def id_voo(self,id_voo):
        self.__id_voo = id_voo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo
    
    @distancia.setter
    def distancia(self,distancia):
        self.__distancia = distancia 
    
    @numero_passageiros.setter
    def numero_passageiros(self,numero_passageiros):
        self.__numero_passageiros = numero_passageiros
    
    @peso.setter
    def peso(self,peso):
        self.__peso = peso
    
    @aeronave.setter
    def aeronave(self,aeronave):
        self.__aeronave = aeronave    
   
    
    
        