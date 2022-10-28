from tela_abstrata import TelaAbstrata

class TelaPassageiro(TelaAbstrata):
    def __init__(self):
        super().__init__()
    
    
  def tela_opcoes(self):
    print("-------- passageiros ----------")
    print("Escolha a opcao")
    print("1 - Incluir passageiro")
    print("2 - Alterar passageiro")
    print("3 - Listar passageiros")
    print("4 - Excluir passageiro")
    print("0 - Retornar")

    opcao = self.le numofae
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_aeronave(self):
    print("-------- DADOS passageiro ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    return {"nome": nome, "telefone": telefone, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_ṕassageiro(self, dados_aeronave):
    print("NOME DO passageiro: ", dados_aeronave["nome"])
    print("FONE DO passageiro: ", dados_aeronave["telefone"])
    print("CPF DO passageiro: ", dados_aeronave["cpf"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_passageiro(self):
    cpf = input("CPF do passageiro que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)