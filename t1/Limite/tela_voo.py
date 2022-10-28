from Limite.tela_abstrata import TelaAbstrata


class TelaVoo(TelaAbstrata):
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  tela_sistema = TelaAbstrata()
  def tela_opcoes(self):
    print("-------- Voos ----------")
    print("Escolha a opcao")
    print("1 - Incluir voo")
    print("2 - Alterar voo")
    print("3 - Listar voos")
    print("4 - Excluir voo")
    print("5 - Incluir passageiros")
    print("6 - Excluir passageiros")
    print("7 - Listar passageiros")
    print("0 - Retornar")

    
    opcao = self.tela_sistema.le_num_inteiro()
    
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_voo(self):
    print("-------- DADOS voo ----------")
    id = input("ID: ")
    data = input("Data: ")
     
    return {"id": id, "data": data, 
            
            }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_voo(self, dados_voo):
    print("ID DO VOO: ", dados_voo["id"])
    print("DATA DO VOO: ", dados_voo["data"])
    
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_voo(self):
    id = input("ID do voo que deseja selecionar: ")
    return id

  def mostra_mensagem(self, msg):
    print(msg)