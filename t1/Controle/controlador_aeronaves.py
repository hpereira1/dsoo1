from Limite.tela_aeronave import TelaAeronave
from Entidade.aeronave import Aeronave


class ControladorAeronaves():

  def __init__(self, controlador_sistema):
    self.__aeronaves = []
    self.__tela_aeronave = TelaAeronave()
    self.__controlador_sistema = controlador_sistema

#   def pega_Aeronave_por_cpf(self, cpf: int):
#     for Aeronave in self.__Aeronaves:
#       if(Aeronave.cpf == cpf):
#         return Aeronave
#     return None

#   #testagem com lançamento de exceção para Aeronaves já existentes!
#   def incluir_aeronave(self):
#     dados_aeronave = self.__tela_aeronave.pega_dados_aeronave()
#     Aeronave = self.pega_Aeronave_por_cpf(dados_Aeronave["cpf"])
#     try:
#       if Aeronave == None:
#         Aeronave = Aeronave(dados_Aeronave["nome"], dados_Aeronave["telefone"], dados_Aeronave["cpf"])
#         self.__Aeronaves.append(Aeronave)
#       else:
#         raise KeyError
#     except KeyError:
#       self.__tela_Aeronave.mostra_mensagem("Aeronave já existente!")

#   def alterar_Aeronave(self):
#     self.lista_Aeronaves()
#     cpf_Aeronave = self.__tela_Aeronave.seleciona_Aeronave()
#     Aeronave = self.pega_Aeronave_por_cpf(cpf_Aeronave)

#     if(Aeronave is not None):
#       novos_dados_Aeronave = self.__tela_Aeronave.pega_dados_Aeronave()
#       Aeronave.nome = novos_dados_Aeronave["nome"]
#       Aeronave.telefone = novos_dados_Aeronave["telefone"]
#       Aeronave.cpf = novos_dados_Aeronave["cpf"]
#       self.lista_Aeronaves()
#     else:
#       self.__tela_Aeronave.mostra_mensagem("ATENCAO: Aeronave não existente")

#   # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
#   def lista_Aeronaves(self):
#     for Aeronave in self.__Aeronaves:
#       self.__tela_Aeronave.mostra_Aeronave({"nome": Aeronave.nome, "telefone": Aeronave.telefone, "cpf": Aeronave.cpf})

  def excluir_Aeronave(self):
    self.lista_Aeronaves()
    cpf_Aeronave = self.__tela_Aeronave.seleciona_Aeronave()
    Aeronave = self.pega_Aeronave_por_cpf(cpf_Aeronave)

    if(Aeronave is not None):
      self.__Aeronaves.remove(Aeronave)
      self.lista_Aeronaves()
    else:
      self.__tela_Aeronave.mostra_mensagem("ATENCAO: Aeronave não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_Aeronave, 2: self.alterar_Aeronave, 3: self.lista_Aeronaves, 4: self.excluir_Aeronave, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_Aeronave.tela_opcoes()]()