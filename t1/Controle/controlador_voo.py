   
from Limite.tela_voo import TelaVoo
from Entidade.voo import Voo

class ControladorVoos:

  def __init__(self, controlador_sistema):
    self.__passageiros = ["Eduardo", "Joao", "Bolsonaro","Lula","Henrique"]
    self.__voos = []
    self.__tela_voo = TelaVoo()
    self.__controlador_sistema = controlador_sistema
  
  @property
  def tela_voo(self):
    return self.__tela_voo

  def pega_voo_por_id(self, id: str):
    for voo in self.__voos:
      if(voo.id == id):
        return voo
    return None
      
  def incluir_voo(self):
      dados_voo = self.tela_voo.pega_dados_voo()
      voo = self.pega_voo_por_id(dados_voo["id"])
      try:
        if voo == None:

          voo = Voo(
                              dados_voo["id"], dados_voo["data"]
                              )
          self.__voos.append(voo)
          while True:
            self.incluir_passageiro(voo)
            aux = input(self.tela_voo.mostra_mensagem("incluir mais passageiros? "))
            if aux in "NAOnao":
              break
          while True:
            self.incluir_tripulante(voo)
            aux1 = input(self.tela_voo.mostra_mensagem("incluir mais funcionario? "))
            if aux1 in "NAOnao":
              break
          self.tela_voo.mostra_mensagem("\nCRIANDO PLANO DE VOO\n")
          numero_passageiros = len(voo.passageiros_voo)
          self.__controlador_sistema.controlador_planos_de_voo.incluir_plano_de_voo(dados_voo["id"],numero_passageiros)
            
        
        else:
          raise KeyError
      except KeyError:
        self.__tela_voo.mostra_mensagem("Voo já existente!")
          
  def alterar_voo(self):
    try:
      if not self.__voos:
        raise Exception
      else:
        self.lista_voos()
        id_voo = self.__tela_voo.seleciona_voo()
        voo = self.pega_voo_por_id(id_voo)
        
        if(voo is not None):
          novos_dados_voo = self.__tela_voo.pega_dados_voo()
          voo.id = novos_dados_voo["id"]
          voo.data = novos_dados_voo["data"] 
          
        else:
          self.__tela_voo.mostra_mensagem("ATENCAO: voo não existente")
    except Exception:
      self.__tela_voo.mostra_mensagem("\nNENHUM  VOO ENCONTRADO!\n")

  # # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_voos(self):
    dados_voo = []
    try:
      if not self.__voos:
        raise Exception
      else:
        for voo in self.__voos:
          dados_voo.append({"id": voo.id, "data": voo.data, "plano_de_voo": voo.plano_de_voo.codigo, "passageiros_voo": voo.passageiros_voo, "tripulantes_voo": voo.tripulantes_voo})
          self.__tela_voo.mostra_voo(dados_voo)          
          self.__tela_voo.detalhes()
    except Exception:
      self.__tela_voo.mostra_mensagem("\nNENHUM  VOO ENCONTRADO!\n")
    

  def incluir_passageiro(self,voo):
      #self.tela_voo.mostra_mensagem(self.controlador_sistema.controlador_passageiros.passageiros)
      self.__controlador_sistema.controlador_passageiros.lista_passageiros()
      passageiro = self.__controlador_sistema.controlador_passageiros.pega_passageiro_por_id(self.tela_voo.entrada("Digite o id de um passageiro"))
      voo.passageiros_voo.append(passageiro)
      passageiro.historico_de_voos.append(voo)

  def incluir_tripulante(self,voo):
      #self.tela_voo.mostra_mensagem(self.controlador_sistema.controlador_passageiros.passageiros)
      self.__controlador_sistema.controlador_funcionarios.lista_funcionarios()
      funcionario = self.__controlador_sistema.controlador_funcionarios.pega_funcionario_por_id(self.tela_voo.entrada("Digite o id de um funcionario"))
      voo.tripulantes_voo.append(funcionario)
  
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
                    5: self.lista_plano,
                    
                    0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_voo.tela_opcoes()]()
  
  
    
    