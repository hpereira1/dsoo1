from Limite.tela_sistema import TelaSistema
from Controle.controlador_aeronaves import ControladorAeronaves

class ControladorSistema:

    def __init__(self):
        self.__controlador_aeronaves = ControladorAeronaves(self)
        self.__tela_sistema = TelaSistema()
        
        

    @property
    def controlador_aeronaves(self):
        return self.__controlador_aeronaves

    

    def inicializa_sistema(self):
        self.abre_tela()

   

    def cadastra_aeronaves(self):                
        self.__controlador_aeronaves.abre_tela()


    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_aeronaves, 0: self.encerra_sistema}
        

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()