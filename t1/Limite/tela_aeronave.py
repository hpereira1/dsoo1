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

    
    opcao = self.tela_sistema.le_num_inteiro()
    
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_aeronave(self):
    print("-------- DADOS aeronave ----------")
    codigo = input("Codigo: ")
    modelo = input("Modelo: ")
    combustivel = input("Combustivel (kg): ")
    numero_max_passageiros = input("Numero maximo de passageiros: ")
    peso_max_decolagem = input("Peso maximo de decolagem (kg): ")
    distancia_maxima = input("Distancia maxima (km): ")
    numero_min_tripulantes = input("Numero minimo de tripulantes: ")
    
    return {"codigo": codigo, "modelo": modelo, 
            "combustivel":combustivel, "numero_max_passageiros": numero_max_passageiros, 
            "peso_max_decolagem": peso_max_decolagem, "distancia_maxima":distancia_maxima, "numero_min_tripulantes":numero_min_tripulantes
            }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_aeronave(self, dados_aeronave):
    print("CODIGO DA aeronave: ", dados_aeronave["codigo"])
    print("MODELO DA aeronave: ", dados_aeronave["modelo"])
    #print("CPF DO aeronave: ", dados_aeronave["cpf"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_aeronave(self):
    codigo = input("Codigo do aeronave que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)