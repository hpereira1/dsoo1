from Limite.tela_passageiro import TelaPassageiro
from Entidade.passageiro import Passageiro


class ControladorPassageiros:
    def __init__(self, controlador_sistema):
        self.__passageiros = ["a","b"]
        self.__tela_passageiro = TelaPassageiro()
        self.__controlador_sistema = controlador_sistema
        
    def iniciar(self):
        self.abre_tela()
    
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    
    def pega_passageiro_por_id(self, id: str):
        for passageiro in self.__passageiros:
            if(passageiro.id == id):
                return passageiro
        return None

    
    def inclui_passageiro(self):
        dados_passageiro = self.__tela_passageiro.pega_dados_passageiro()
        passageiro = self.pega_passageiro_por_id(dados_passageiro["id"])
        try:
            if passageiro == None:
                passageiro = Passageiro(dados_passageiro["nome"], dados_passageiro["id"],dados_passageiro["email"])
                self.__passageiros.append(passageiro)
                self.lista_passageiros()
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
                self.lista_passageiros()
            else:
                raise Exception
        except Exception:
            self.__tela_passageiro.mostra_mensagem("passageiro nao existe")
    
    def altera_passageiro(self):
        self.lista_passageiros()
        id_passageiro = self.__tela_passageiro.seleciona_passageiro()
        passageiro = self.pega_passageiro_por_id(id_passageiro)
        try:
            if passageiro is not None:
                novos_dados_passageiro = self.__tela_passageiro.pega_dados_passageiro()
                passageiro.nome = novos_dados_passageiro["nome"]
                passageiro.id = novos_dados_passageiro["id"]
                passageiro.email = novos_dados_passageiro["email"]
                self.lista_passageiros()
            else:
                raise Exception
        except Exception:
            self.__tela_passageiro.mostra_mensagem("Passageiro não existe")
    
    def lista_passageiros(self):
        try:
            if not self.__passageiros:
                raise Exception
            else:        
                for passageiro in self.__passageiros:
                    self.__tela_passageiro.mostra_mensagem({"nome": passageiro.nome, "id": passageiro.id})
        except Exception:
            self.__tela_passageiro.mostra_mensagem("\nNENHUM PASSAGEIRO ENCONTRADO!\n")             
            
    def ver_historico_por_id(self):
        id_passageiro = self.__tela_passageiro.seleciona_passageiro()
        passageiro = self.pega_passageiro_por_id(id_passageiro)
        try:
            if(passageiro is not None):
                for voo in passageiro.__historico_de_voos:
                    self.__tela_passageiro.mostra_mensagem({"id": voo.__id, "data": voo.__data})
            else:
                raise Exception
        except Exception:
            self.__tela_passageiro.mostra_mensagem("passageiro nao existe")
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_passageiro, 2: self.altera_passageiro, 3: self.lista_passageiros, 4: self.remove_passageiro,5: self.pega_passageiro_por_id,6: self.ver_historico_por_id, 0: self.finalizar}    
        continua = True
        while continua:
            lista_opcoes[self.__tela_passageiro.tela_opcoes()]()