from Limite.tela_abstrata import TelaAbstrata


class TelaVoo(TelaAbstrata):
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  tela_sistema = TelaAbstrata()
  def tela_opcoes(self):
    print("-------- Voos ----------")
    print("Escolha a opcao\n")
   
    
    print("1 - Incluir voo")       
    print("2 - Alterar voo")
    print("3 - Listar voos")
    print("4 - Excluir voo")
    print("5 - Listar planos de voo")
    print("0 - Retornar")

    
    opcao = self.tela_sistema.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
    
    return opcao
  
  def entrada(self,arg):
    print(arg)
    entrada = input(">")
    
    return entrada
  
  
  
    

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
    print("PLANO DE VOO: ", dados_voo["plano_de_voo"])
    print("lista passageiros: ", dados_voo["passageiros_voo"])
    print("lista tripulacao: ", dados_voo["tripulantes_voo"])
    
    print("\n")




  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_voo(self):
    id = input("ID do voo que deseja selecionar: ")
    return id


  def mostra_mensagem(self, msg):
    print(msg)