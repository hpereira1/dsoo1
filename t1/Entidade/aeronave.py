class Aeronave:
    def __init__(self, codigo:int, modelo:int, combustivel:int, numero_max_passageiros: int, peso_max_decolagem: int, distancia_maxima: int, numero_min_tripulates: int):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__combustivel = combustivel
        self.__numero_max_passageiros = numero_max_passageiros
        self.__peso_max_decolagem = peso_max_decolagem
        self.__distancia_maxima = distancia_maxima
        self.__numero_min_tripulates = numero_min_tripulates
        self._historico_de__voos = {}


    @property
    def codigo(self):
        return self.__codigo
   
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def combustivel(self):
        return self.__combustivel
    
    @property
    def numero_max_passageiros(self):
        return self.__numero_max_passageiros
  
    @property
    def peso_max_decolagem(self):
        return self.__peso_max_decolagem
  
    @property
    def distancia_maxima(self):
        return self.__distancia_maxima
   
    @property
    def numero_min_tripulates(self):
        return self.__numero_min_tripulates
   
    @property
    def historico_de__voos(self):
        return self.__historico_de__voos

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
   
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
   
    @combustivel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel
   
    @numero_max_passageiros.setter
    def numero_max_passageiros(self, numero_max_passageiros):
        self.__numero_max_passageiros = numero_max_passageiros
   
    @peso_max_decolagem.setter
    def peso_max_decolagem(self, peso_max_decolagem):
        self.__peso_max_decolagem = peso_max_decolagem
   
    @distancia_maxima.setter
    def distancia_maxima(self, distancia_maxima):
        self.__distancia_maxima = distancia_maxima
   
    @numero_min_tripulates.setter
    def numero_min_tripulates(self, numero_min_tripulates):
        self.__numero_min_tripulates = numero_min_tripulates
   
    @historico_de__voos.setter
    def historico_de__voos(self, historico_de__voos):
        self.__historico_de__voos = historico_de__voos