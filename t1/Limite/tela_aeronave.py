from Limite.tela_abstrata import TelaAbstrata


class TelaAeronave(TelaAbstrata):
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  tela_sistema = TelaAbstrata()
  def tela_opcoes(self):
    print("-------- Aeronaves ----------")
    print("Escolha a opcao")
    print("1 - Incluir aeronave")
    print("2 - Alterar aeronave")
    print("3 - Listar aeronaves")
    print("4 - Excluir aeronave")
    print("0 - Retornar")

    
    opcao = self.tela_sistema.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4])
    
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_aeronave(self):
    print("-------- DADOS aeronave ----------")
    codigo = input("Codigo: ")
    modelo = input("Modelo: ")
    combustivel = self.tela_sistema.le_num_inteiro("Combustivel (kg): ")
    numero_max_passageiros = self.tela_sistema.le_num_inteiro("Numero maximo passageiros: ")
    peso_max_decolagem = self.tela_sistema.le_num_inteiro("Peso maximo decolagem (kg): ")
    distancia_maxima = self.tela_sistema.le_num_inteiro("Distancia maxima (km): ")
    numero_min_tripulantes = self.tela_sistema.le_num_inteiro("Numero minimo tripulantes: ")
    #combustivel = input("Combustivel (kg): ")
    #self.tela_sistema.sao_numeros(combustivel)
    #numero_max_passageiros = input("Numero maximo de passageiros: ")    
    #peso_max_decolagem = input("Peso maximo de decolagem (kg): ")
    #distancia_maxima = input("Distancia maxima (km): ")
    #numero_min_tripulantes = input("Numero minimo de tripulantes: ")
    
    return {"codigo": codigo, "modelo": modelo, 
            "combustivel":combustivel, "numero_max_passageiros": numero_max_passageiros, 
            "peso_max_decolagem": peso_max_decolagem, "distancia_maxima":distancia_maxima, "numero_min_tripulantes":numero_min_tripulantes
            }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_aeronave(self, dados_aeronave):
    print("Codigo da aeronave: ", dados_aeronave["codigo"])
    print("Modelo da aeronave: ", dados_aeronave["modelo"])
    print("Combustivel da aeronave: ", dados_aeronave["combustivel"])
    print("Numero maximo de passageiros: ", dados_aeronave["numero_max_passageiros"])
    print("Peso maximo de decolagem: ", dados_aeronave["peso_max_decolagem"])
    print("Distancia maxima: ", dados_aeronave["distancia_maxima"])
    print("Numero minimo de tripulantes: ", dados_aeronave["numero_min_tripulantes"])
   
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_aeronave(self):
    codigo = input("Codigo do aeronave que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)