from Limite.tela_passageiro import TelaPassageiro
from Entidade.passageiro import Passageiro
from DAOs.passageiro_dao import PassageiroDAO


class ControladorPassageiros:
    def __init__(self, controlador_sistema):
        # self.__passageiros = []
        self.__passageiro_DAO = PassageiroDAO()
        self.__tela_passageiro = TelaPassageiro()
        self.__controlador_sistema = controlador_sistema
        
    @property
    def passageiros(self):
        return self.__passageiros
    
    @property
    def tela_passageiro(self):
        return self.__tela_passageiro
    
    
    
        
    def iniciar(self):
        self.abre_tela()
    
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    
    def pega_passageiro_por_id(self, id):
        for passageiro in self.__passageiro_DAO.get_all():
            if(passageiro.id == id):
                return passageiro
        return None

    
    def inclui_passageiro(self):
        dados_passageiro = self.__tela_passageiro.pega_dados_passageiro()
        passageiro = self.pega_passageiro_por_id(dados_passageiro["id"])
        try:
            if passageiro == None:
                passageiro = Passageiro(dados_passageiro["nome"], dados_passageiro["id"],dados_passageiro["email"])
                # self.__passageiros.append(passageiro)
                self.__passageiro_DAO.add(passageiro)
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
                # self.__passageiros.remove(passageiro)
                self.__passageiro_DAO.remove(passageiro.id)
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
                self.__passageiro_DAO.update(passageiro)
                self.lista_passageiros()
            else:
                raise Exception
        except Exception:
            self.__tela_passageiro.mostra_mensagem("Passageiro não existe")
    
    
    def lista_passageiros(self):
        dados_passageiro = []
        try:
            if not self.__passageiro_DAO.get_all():
                raise Exception
            else:        
                for passageiro in self.__passageiro_DAO.get_all():
                    dados_passageiro.append({"nome": passageiro.nome, "id": passageiro.id,"email": passageiro.email})
                    #self.__tela_passageiro.mostra_mensagem({"nome": passageiro.nome, "id": passageiro.id})
                self.__tela_passageiro.mostra_passageiro(dados_passageiro,False)
        except Exception:
            self.__tela_passageiro.mostra_mensagem("\nNENHUM PASSAGEIRO SELECIONADO!\n")
    
    def lista_passageiros2(self):
        dados_passageiro = []             
        for passageiro in self.__passageiro_DAO.get_all():
            dados_passageiro.append({"nome": passageiro.nome, "id": passageiro.id,"email": passageiro.email})
            #self.__tela_passageiro.mostra_mensagem({"nome": passageiro.nome, "id": passageiro.id})
        x = self.__tela_passageiro.mostra_passageiro(dados_passageiro,True)
        return x
        
            
    def seleciona_passageiro(self,id):
        dados_passageiro = []
        for passageiro in self.__passageiro_DAO.get_all():
            if passageiro.id == id:
                    dados_passageiro.append({"nome": passageiro.nome, "id": passageiro.id,"email": passageiro.email})
        self.__tela_passageiro.mostra_passageiro(dados_passageiro,True)             
            
    def ver_historico_por_id(self):
        self.lista_passageiros()
        id_passageiro = self.__tela_passageiro.seleciona_passageiro()
        passageiro = self.pega_passageiro_por_id(id_passageiro)
        try:
            if(passageiro is not None):
                for voo in passageiro.historico_de_voos:
                    self.__tela_passageiro.mostra_mensagem({"id": voo.id, "data": voo.data})
            else:
                raise Exception
        except Exception:
            self.__tela_passageiro.mostra_mensagem("passageiro nao existe")
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_passageiro, 2: self.altera_passageiro, 3: self.lista_passageiros, 4: self.remove_passageiro,6: self.pega_passageiro_por_id,5: self.ver_historico_por_id, 0: self.finalizar}    
        continua = True
        while continua:
            lista_opcoes[self.__tela_passageiro.tela_opcoes()]()