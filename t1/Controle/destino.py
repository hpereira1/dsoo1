import Controle.controlador_voo 
#from Controle.controlador_voo import ControladorVoos

def menu_destino():   
    return Controle.controlador_voo.TelaVoo().tela_destino()

      
          
       
        
def retornar2(self):
    self.__controlador_sistema.controlador_voo.abre_tela2()



def abre_tela2(self):
    lista_opcoes = { 0: self.retornar, 3: self.lista_destinos1}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_voo.tela_opcoes()]()
    