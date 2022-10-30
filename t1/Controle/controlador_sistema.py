import imp
from Limite.tela_sistema import TelaSistema
from Controle.controlador_aeronaves import ControladorAeronaves
from Controle.controlador_planos_de_voo import ControladorPlanosDeVoo
from Controle.controlador_voo import ControladorVoos
from Controle.controlador_passageiros import ControladorPassageiros
from Controle.controlador_funcionarios import ControladorFuncionarios
class ControladorSistema:

    def __init__(self):
        self.__controlador_aeronaves = ControladorAeronaves(self)
        self.__controlador_planos_de_voo = ControladorPlanosDeVoo(self)
        self.__controlador_voo = ControladorVoos(self)
        self.__controlador_passageiros = ControladorPassageiros(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__tela_sistema = TelaSistema()
        
        

    @property
    def controlador_aeronaves(self):
        return self.__controlador_aeronaves
    
    @property
    def controlador_planos_de_voo(self):
        return self.__controlador_planos_de_voo
    
    @property
    def controlador_voo(self):
        return self.__controlador_voo
    
    @property
    def controlador_passageiros(self):
        return self.__controlador_passageiros

    @property
    def controlador_funcionarios(self):
        return self.__controlador_funcionarios

    def inicializa_sistema(self):
        self.abre_tela()

   

    def cadastra_aeronaves(self):                
        self.__controlador_aeronaves.abre_tela()
    
    def plano_de_voo(self):
        self.__controlador_planos_de_voo.lista_planos_de_voos()
    
    def voo(self):
        self.__controlador_voo.abre_tela()
    
    def passageiros(self):
        self.__controlador_passageiros.abre_tela()
        
    def funcionarios(self):
        self.__controlador_funcionarios.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_aeronaves, 2: self.voo, 3: self.plano_de_voo, 4: self.passageiros, 5: self.funcionarios, 0: self.encerra_sistema}
        

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()