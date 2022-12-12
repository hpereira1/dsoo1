from Limite.tela_funcionario import TelaFuncionario
from Entidade.funcionario import Funcionario
from Entidade.cargo import Cargo
from DAOs.cargo_dao import CargoDAO
from DAOs.funcionario_dao import FuncionarioDAO
class ControladorFuncionarios:
    def __init__(self, controlador_sistema):
        #self.__funcionarios = []
        self.__funcionario_DAO = FuncionarioDAO()
        self.__cargo_DAO = CargoDAO()
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema
        #self.__cargos = [Cargo("PILOTO", "0", 10000), Cargo("COMISSARIO", "1" , 3000)]
        
    def iniciar(self):
        self.abre_tela()
    
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    
    def pega_cargo_por_id(self, id: str):
        for cargo in self.__cargo_DAO.get_all():
            if(cargo.id == id):
                return cargo
        return None
    
    def pega_funcionario_por_id(self, id: str):
        for funcionario in self.__funcionario_DAO.get_all():
            if(funcionario.id == id):
                return funcionario
        return None

    
    def inclui_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        funcionario = self.pega_funcionario_por_id(dados_funcionario["id"])
        try:
            if funcionario == None:
                self.lista_cargos()
                dados_funcionario["cargo"] = self.__tela_funcionario.seleciona_cargo()
                funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["id"],dados_funcionario["email"], dados_funcionario["cargo"])
                # self.__funcionarios.append(funcionario)
                self.__funcionario_DAO.add(funcionario)
                self.lista_funcionarios()
            else:
                raise KeyError
        except KeyError:
            self.__tela_funcionario.mostra_mensagem("funcionario já existente!")

    
    def remove_funcionario(self):
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_id(id_funcionario)
        try:
            if (funcionario is not None):
                # self.__funcionarios.remove(funcionario)
                self.__funcionario_DAO.remove(funcionario.id)
                self.lista_funcionarios()
            else:
                raise Exception
        except Exception:
            self.__tela_funcionario.mostra_mensagem("funcionario nao existe")
    
    def altera_funcionario(self):
        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_id(id_funcionario)
        try:
            if funcionario is not None:
                novos_dados_cargo = self.__tela_funcionario.pega_dados_funcionario()
                funcionario.nome = novos_dados_cargo["nome"]
                funcionario.id = novos_dados_cargo["id"]
                funcionario.email = novos_dados_cargo["email"]
                self.lista_cargos()
                id_cargo = self.__tela_funcionario.seleciona_cargo()
                funcionario.cargo = self.pega_cargo_por_id(id_cargo)
                self.__funcionario_DAO.update(funcionario)
                self.lista_funcionarios()
            else:
                raise Exception
        except Exception:
            self.__tela_funcionario.mostra_mensagem("funcionario não existe")
    
    def lista_funcionarios(self):
        try:
            if not self.__funcionario_DAO.get_all():
                raise Exception
            else:        
                for funcionario in self.__funcionario_DAO.get_all():
                    self.__tela_funcionario.mostra_mensagem({"nome": funcionario.nome, "id": funcionario.id, "cargo": funcionario.cargo,
                                                             "email": funcionario.email})
        except Exception:
            self.__tela_funcionario.mostra_mensagem("\nNENHUM funcionario ENCONTRADO!\n")             
    
    def lista_funcionarios2(self):
        dados_funcionario = []
        try:
            if not self.__funcionario_DAO.get_all():
                raise Exception                
            else:             
                for funcionario in self.__funcionario_DAO.get_all():
                    dados_funcionario.append({"nome": funcionario.nome, "id": funcionario.id, "cargo": funcionario.cargo,
                                            "email": funcionario.email})           
                    x = self.__tela_funcionario.mostra_funcionario(dados_funcionario,True)
                    return x
        except Exception:
            self.__tela_funcionario.mostra_mensagem("\nNENHUM funcionario ENCONTRADO!\n")
            return 0 
            
    
    
    
    
    
    def lista_cargos(self):
        try:
            if not self.__cargo_DAO.get_all():
                raise Exception
            else:        
                for cargo in self.__cargo_DAO.get_all():
                    self.__tela_funcionario.mostra_mensagem({"descricao": cargo.descricao, "id": cargo.id, "salario": cargo.salario})
        except Exception:
            self.__tela_funcionario.mostra_mensagem("\nNENHUM cargo ENCONTRADO!\n")             
          
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_funcionario, 2: self.altera_funcionario, 3: self.lista_funcionarios, 4: self.remove_funcionario,5: self.criar_cargo, 6: self.alterar_cargo, 7: self.lista_cargos,8: self.remove_cargo, 0: self.finalizar}    
        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
            
    def criar_cargo(self):
        dados_cargo = self.__tela_funcionario.pega_dados_cargo()
        cargo = self.pega_cargo_por_id(dados_cargo["id"])
        try:
            if cargo == None:
                cargo = Cargo(dados_cargo["descricao"], dados_cargo["id"],dados_cargo["salario"])
                # self.__cargos.append(cargo)
                self.__cargo_DAO.add(cargo)
                self.lista_cargos()
            else:
                raise KeyError
        except KeyError:
            self.__tela_funcionario.mostra_mensagem("cargo já existente!")
 
    def alterar_cargo(self):
        self.lista_cargos()
        id_cargo = self.__tela_funcionario.seleciona_cargo()
        cargo = self.pega_cargo_por_id(id_cargo)
        try:
            if cargo is not None:
                novos_dados_cargo = self.__tela_funcionario.pega_dados_cargo()
                cargo.descricao = novos_dados_cargo["descricao"]
                cargo.id = novos_dados_cargo["id"]
                cargo.salario = novos_dados_cargo["salario"]
                self.__cargo_DAO.update(cargo)
                self.lista_cargos()
            else:
                raise Exception
        except Exception:
            self.__tela_funcionario.mostra_mensagem("cargo não existe")
    
    def remove_cargo(self):
        self.lista_cargos()
        id_cargo = self.__tela_funcionario.seleciona_cargo()
        cargo = self.pega_cargo_por_id(id_cargo)
        try:
            if (cargo is not None):
                self.__cargo_DAO.remove(cargo.id)
                self.lista_cargos()
            else:
                raise Exception
        except Exception:
            self.__tela_funcionario.mostra_mensagem("cargo nao existe")
