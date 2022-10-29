from Limite.tela_abstrata import TelaAbstrata


class TelaVoo(TelaAbstrata):
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  tela_sistema = TelaAbstrata()
  def tela_opcoes(self):
    print("-------- Voos ----------")
    print("Escolha a opcao\n")
   
    print("1 - Menu Destinos")
    print("2 - Incluir voo")       
    print("3 - Alterar voo")
    print("4 - Listar voos")
    print("5 - Excluir voo")
    print("6 - Incluir passageiros")
    print("7 - Excluir passageiros")
    print("8 - Listar passageiros")
    print("9 - Listar planos de voo")
    print("0 - Retornar")

    
    opcao = self.tela_sistema.le_num_inteiro()
    
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_voo(self):
    print("-------- DADOS VOO ----------\n")
    
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