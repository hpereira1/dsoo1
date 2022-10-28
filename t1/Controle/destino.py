import Controle.controlador_voo

def menu_destino():
    return Controle.controlador_voo.TelaVoo().tela_destino()

def lista_destinos(self):
    for destino in self.__Controle.controlador_voo.destinos:
      self.__tela_voo.mostra_voo(destino)      
       
        
def retornar2(self):
    self.__controlador_sistema.controlador_voo.abre_tela2()



def abre_tela2(self):
    lista_opcoes = { 0: self.retornar, 3: self.lista_destinhos}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_voo.tela_opcoes()]()
    