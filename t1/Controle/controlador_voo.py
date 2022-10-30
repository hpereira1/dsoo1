   
from Limite.tela_voo import TelaVoo
from Entidade.voo import Voo





class ControladorVoos:

  def __init__(self, controlador_sistema):
    self.__passageiros = ["Eduardo", "Joao", "Bolsonaro","Lula","Henrique"]
    self.__voos = []
    self.__tela_voo = TelaVoo()
    self.__controlador_sistema = controlador_sistema
    
  

  def pega_voo_por_id(self, id: str):
    for voo in self.__voos:
      if(voo.id == id):
        return voo
    return None
  
  
      
    

  #testagem com lançamento de exceção para voos já existentes!
  def incluir_voo(self):
    dados_voo = self.__tela_voo.pega_dados_voo()
    voo = self.pega_voo_por_id(dados_voo["id"])
    try:
      if voo == None:
        
        voo = Voo(
                            dados_voo["id"], dados_voo["data"]
                            )
        self.__voos.append(voo)        
        self.__tela_voo.mostra_mensagem("\nCRIANDO PLANO DE VOO\n")      
        numero_passageiros = len(self.__passageiros)              
        self.__controlador_sistema.controlador_planos_de_voo.incluir_plano_de_voo(dados_voo["id"],numero_passageiros)
        
        
        #self.__tela_voo.mostra_mensagem("\nAERONAVES\n")  
        #self.__controlador_sistema.controlador_aeronaves.lista_aeronaves()
        #self.__controlador_sistema.controlador_planos_de_voo.seleciona_aeronave()
        #voo.aeronave = self.__controlador_sistema.controlador_aeronaves.pega_aeronave_por_codigo(self.__tela_voo.entrada("\nDIGITE O CODIGO DE UM AVIAO\n"))
        
       
        
      else:
        raise KeyError
    except KeyError:
      self.__tela_voo.mostra_mensagem("Voo já existente!")
    
    

      


  def alterar_voo(self):
    self.lista_voos()
    id_voo = self.__tela_voo.seleciona_voo()
    voo = self.pega_voo_por_id(id_voo)
    
    if(voo is not None):
      novos_dados_voo = self.__tela_voo.pega_dados_voo()
      voo.id = novos_dados_voo["id"]
      voo.data = novos_dados_voo["data"]
      
      self.lista_voos()
    else:
      self.__tela_voo.mostra_mensagem("ATENCAO: voo não existente")

  # # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_voos(self):
    try:
      if not self.__voos:
        raise Exception
      else:
        for voo in self.__voos:
          self.__tela_voo.mostra_voo({"id": voo.id, "data": voo.data, "plano_de_voo": voo.plano_de_voo, "aeronave":voo.aeronave})
    except Exception:
      self.__tela_voo.mostra_mensagem("\nNENHUM  VOO ENCONTRADO!\n")
    
    
  def incluir_passageiro(self):
    #self.__tela_voo.mostra_mensagem(self.__controlador_sistema.controlador_passageiros.passageiros)
    self.__controlador_sistema.controlador_passageiros.lista_passageiros()
    passageiro = self.__controlador_sistema.controlador_passageiros.pega_passageiro_por_id(self.__tela_voo.entrada("Digite o id de um passageiro"))
    self.__passageiros.append(passageiro.id)
    self.__controlador_sistema.controlador_passageiros.lista_passageiros()
    
   
  
  
  def excluir_passageiro(self):
    self.__controlador_sistema.controlador_passageiros.lista_passageiros()
    passageiro = self.__controlador_sistema.controlador_passageiros.pega_passageiro_por_id(self.__tela_voo.entrada("Digite o id de um passageiro"))
    self.__passageiros.remove(passageiro.id)
    
  
  def listar_passageiro(self):
    try:
      if not self.__passageiros:
        raise Exception
      else:
        for passageiro in self.__passageiros:
          self.__tela_voo.mostra_mensagem(passageiro)
    except Exception:
      self.__tela_voo.mostra_mensagem("\nNENHUM  PASSAGEIRO ENCONTRADO!\n")
  
  def teste (self):        
    print(self.__controlador_sistema.controlador_passageiros.passageiros)
  
  
  
  
  
  
  def excluir_voo(self):
    self.lista_voos()
    id_voo = self.__tela_voo.seleciona_voo()
    voo = self.pega_voo_por_id(id_voo)

    if(voo is not None):
      self.__voos.remove(voo)
      self.lista_voos()
    else:
      self.__tela_voo.mostra_mensagem("ATENCAO: voo não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()
  
  def lista_plano(self):
    self.__controlador_sistema.controlador_planos_de_voo.lista_planos_de_voos()
    
  def abre_tela(self):
    lista_opcoes = {
                  
                    1: self.incluir_voo, 2: self.alterar_voo, 3: self.lista_voos, 4: self.excluir_voo,
                    5: self.incluir_passageiro, 6: self.excluir_passageiro, 7: self.listar_passageiro,
                    #8: self.teste, 
                    9: self.lista_plano,
                    
                    0: self.retornar}
   
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_voo.tela_opcoes()]()
  
  
    
    