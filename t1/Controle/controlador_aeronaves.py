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
        aeronave = Aeronave(
                            dados_aeronave["codigo"], dados_aeronave["modelo"],dados_aeronave["combustivel"],dados_aeronave["numero_max_passageiros"],
                            dados_aeronave["peso_max_decolagem"],dados_aeronave["distancia_maxima"],dados_aeronave["numero_min_tripulantes"]
                            )
        self.__aeronaves.append(aeronave)
      else:
        raise KeyError
    except KeyError:
      self.__tela_aeronave.mostra_mensagem("Aeronave já existente!")

  def alterar_aeronave(self):
    self.lista_aeronaves()
    codigo_aeronave = self.__tela_aeronave.seleciona_aeronave()
    aeronave = self.pega_aeronave_por_codigo(codigo_aeronave)
    
    if(aeronave is not None):
      novos_dados_aeronave = self.__tela_aeronave.pega_dados_aeronave()
      aeronave.codigo = novos_dados_aeronave["codigo"]
      aeronave.modelo = novos_dados_aeronave["modelo"]
      aeronave.combustivel = novos_dados_aeronave["combustivel"]
      aeronave.numero_max_passafeiros = novos_dados_aeronave["numero_max_passageiros"]
      aeronave.peso_max_decolagem = novos_dados_aeronave["peso_max_decolagem"]
      aeronave.distancia_maxima = novos_dados_aeronave["distancia_maxima"]
      aeronave.numero_min_tripulantes = novos_dados_aeronave["numero_min_tripulantes"]
      aeronave.status = novos_dados_aeronave["status"]
    
      self.lista_aeronaves()
    else:
      self.__tela_aeronave.mostra_mensagem("ATENCAO: Aeronave não existente")

  # # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_aeronaves(self):
    try:
      if not self.__aeronaves:
        raise Exception
      else:        
        for aeronave in self.__aeronaves:
          self.__tela_aeronave.mostra_mensagem({"codigo": aeronave.codigo, "modelo":aeronave.modelo,
                                                "distancia_maxima":aeronave.distancia_maxima,
                                               "status":aeronave.status
                                               })         
    except Exception:
      self.__tela_aeronave.mostra_mensagem("\nNENHUMA AERONAVE ENCONTRADA!!\n")   
      
  def seleciona_aeronave(self,distancia:str):
    try:
      if not self.__aeronaves:
        raise Exception
      else:
          
        for aeronave in self.__aeronaves:
                  
            if (int(aeronave.distancia_maxima) >= int (distancia)) and (aeronave.status == "Livre"):            
              self.__tela_aeronave.mostra_mensagem({"codigo": aeronave.codigo, "modelo":aeronave.modelo, 
                                                  "distancia_maxima":aeronave.distancia_maxima,
                                                  "status":aeronave.status})
        
        self.__controlador_sistema.controlador_planos_de_voo.inclui_aeronave_plano()                  
              
    except Exception:
      self.__tela_aeronave.mostra_mensagem("\nNENHUMA AERONAVE ENCONTRADA\n")
                 
               
        

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
    lista_opcoes = {1: self.incluir_aeronave, 2: self.alterar_aeronave, 3: self.lista_aeronaves, 4: self.excluir_aeronave, 0: self.retornar}
   
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_aeronave.tela_opcoes()]()