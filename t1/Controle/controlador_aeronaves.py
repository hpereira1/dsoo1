from Limite.tela_aeronave import TelaAeronave
from Entidade.aeronave import Aeronave


class ControladorAeronaves():

  def __init__(self, controlador_sistema):
    self.__aeronaves = []
    self.__tela_aeronave = TelaAeronave()
    self.__controlador_sistema = controlador_sistema

  def pega_aeronave_por_codigo(self, codigo: str):
    for aeronave in self.__aeronaves:
      if(aeronave.codigo == codigo):
        return aeronave
    return None

  #testagem com lançamento de exceção para Aeronaves já existentes!
  def incluir_aeronave(self):
    dados_aeronave = self.__tela_aeronave.pega_dados_aeronave()
    aeronave = self.pega_aeronave_por_codigo(dados_aeronave["codigo"])
    try:
      if aeronave == None:
        aeronave = aeronave(dados_aeronave["codigo"], dados_aeronave["modelo"], dados_aeronave["combustivel"], dados_aeronave["numero_max_passageiros"],
                            dados_aeronave["peso_max_decolagem"],dados_aeronave["distancia_max"],dados_aeronave["numero_min_tripulantes"])
        self.__aeronaves.append(aeronave)
      else:
        raise KeyError
    except KeyError:
      self.__tela_aeronave.mostra_mensagem("Aeronave já existente!")

  # def alterar_aeronave(self):
  #   self.lista_aeronaves()
  #   cpf_Aeronave = self.__tela_aeronave.seleciona_Aeronave()
  #   Aeronave = self.pega_Aeronave_por_cpf(cpf_Aeronave)

  #   if(Aeronave is not None):
  #     novos_dados_aeronave = self.__tela_aeronave.pega_dados_aeronave()
  #     Aeronave.nome = novos_dados_aeronave["nome"]
  #     Aeronave.telefone = novos_dados_aeronave["telefone"]
  #     Aeronave.cpf = novos_dados_aeronave["cpf"]
  #     self.lista_Aeronaves()
  #   else:
  #     self.__tela_aeronave.mostra_mensagem("ATENCAO: Aeronave não existente")

  # # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  # def lista_aeronaves(self):
  #   for aeronave in self.__aeronaves:
  #     self.__tela_aeronave.mostra_Aeronave({"nome": Aeronave.nome, "telefone": Aeronave.telefone, "cpf": Aeronave.cpf})

  def excluir_aeronave(self):
    self.lista_aeronaves()
    codigo_aeronave = self.__tela_aeronave.seleciona_aeronave()
    aeronave = self.pega_aeronave_por_codigo(codigo_aeronave)

    if(aeronave is not None):
      self.__aeronaves.remove(aeronave)
      self.lista_aeronaves()
    else:
      self.__tela_aeronave.mostra_mensagem("ATENCAO: Aeronave não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    #lista_opcoes = {1: self.incluir_aeronave, 2: self.alterar_aeronave, 3: self.lista_aeronaves, 4: self.excluir_aeronave, 0: self.retornar}
    lista_opcoes = {1: self.incluir_aeronave, 4: self.excluir_aeronave, 0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_aeronave.tela_opcoes()]()