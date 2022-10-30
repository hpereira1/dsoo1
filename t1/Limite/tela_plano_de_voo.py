
from Limite.tela_abstrata import TelaAbstrata


class TelaPlanoDeVoo(TelaAbstrata):
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- PLANOS DE VOO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Plano de Voo")
        print("2 - Alterar Plano de Voo")
        print("3 - Listar Planos de Voo")
        print("4 - Excluir Plano de Voo")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_plano_de_voo(self):
        print("-------- DADOS PLANOS DE VOO ----------")
        #id_voo = input("ID_VOO: ")
        codigo = input("CODIGO: ")
        distancia = input("Distancia: ")
        #numero_passageiros = input("Numero de passageiros: ")
        peso = input("Peso: ")        
        #aeronave = input("Aeronave: ")

        return {"codigo": codigo, "distancia": distancia, 
                #"numero_passageiros": numero_passageiros, 
                "peso": peso, 
                #"aeronave":aeronave
                 }
    
    def entrada(self,arg):
      print(arg)
      entrada = input(">")
      return entrada

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_plano_de_voo(self, dados_plano_de_voo):
        print("\n\n\n")
        print("ID do Voo: ", dados_plano_de_voo["id_voo"])
        print("Codigo do Plano de Voo: ", dados_plano_de_voo["codigo"])
        print("DISTANCIA do Voo: ", dados_plano_de_voo["distancia"])
        print("Numero de passageiros do Voo: ", dados_plano_de_voo["numero_passageiros"])
        print("Peso do Voo: ", dados_plano_de_voo["peso"])
        print("Aeronave do voo: ", dados_plano_de_voo["aeronave"])
        print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_plano_de_voo(self):
        codigo = input("CODIGO do Plano de Voo que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)