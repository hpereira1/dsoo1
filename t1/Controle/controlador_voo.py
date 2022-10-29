   
from Limite.tela_voo import TelaVoo
from Entidade.voo import Voo
import Controle.destino




class ControladorVoos:

  def __init__(self, controlador_sistema):
    #self.__destinos = ['Sao Paulo','Rio','Brasilia']
    self.__destinos = [{'Sao Paulo':700},{'Rio':1200},{'Brasilia':2100}]
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
        self.__tela_voo.mostra_mensagem("\nESCOLHA O DESTINO\n")
        self.__controlador_sistema.controlador_voo.lista_destinos()
       
        #self.__controlador_sistema.controlador_planos_de_voo.incluir_plano_de_voo(voo.id)
        
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
    for voo in self.__voos:
      self.__tela_voo.mostra_voo({"id": voo.id, "data": voo.data})
  
  # # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_destinos(self):
    for destino in self.__destinos:
      self.__tela_voo.mostra_mensagem(destino)

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
  
  def lista_planos(self):
    self.__controlador_sistema.controlador_planos_de_voo.lista_planos_de_voos()
    
  ###############################################
  
    
  ######################################################
    

  def abre_tela(self):
    lista_opcoes = {1: Controle.destino.menu_destino, 
                    2: self.incluir_voo, 3: self.alterar_voo, 4: self.lista_voos, 4: self.excluir_voo, 
                    9: self.lista_planos,
                    7:self.lista_destinos, 
                    0: self.retornar}
   
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_voo.tela_opcoes()]()
  
  
    
    