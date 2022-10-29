from Limite.tela_passageiro import TelaPassageiro
from Entidade.passageiro import Passageiro


class ControladorPassageiros:
    def __init__(self, controlador_sistema):
        self.__passageiros = []
        self.__tela_passageiro = TelaPassageiro()
        self.__controlador_sistema = controlador_sistema
        
    def iniciar(self):
        pass
    
    def finalizar(self):
        pass
    
    def abre_tela_inicial(self):
        pass
    
    def pega_passageiro_por_id(self, id: int):
        for passageiro in self.__passageiros:
            if(passageiro.__id == id):
                return passageiro
        return None

    
    def inclui_passageiro(self):
        dados_passageiro = self.__tela_passageiro.pega_dados_passageiro()
        passageiro = self.pega_passageiro_por_id(dados_passageiro["id"])
        try:
            if passageiro == None:
                passageiro = Passageiro(dados_passageiro["nome"], dados_passageiro["id"],dados_passageiro["email"])
                self.__passageiros_.append(passageiro)
            else:
                raise KeyError
        except KeyError:
            self.__tela_passageiro.mostra_mensagem("Passageiro já existente!")

    
    def remove_passageiro(self):
        id_passageiro = self.__tela_passageiro.seleciona_passageiro()
        passageiro = self.pega_passageiro_por_id(id_passageiro)
        try:
            if (passageiro is not None):
                self.__passageiros.remove(passageiro)
            else:
                raise Exception
        except Exception:
            self.__tela_passageiro.mostra_mensagem("passageiro nao existe")
    
    def altera_passageiro(self):
        pass
    
    def lista_passageiros(self):
        pass
    
    def ver_historico_por_id(self):
        pass
    