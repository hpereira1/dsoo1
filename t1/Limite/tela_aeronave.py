
class TelaAeronave():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- aeronaveS ----------")
    print("Escolha a opcao")
    print("1 - Incluir aeronave")
    print("2 - Alterar aeronave")
    print("3 - Listar aeronaves")
    print("4 - Excluir aeronave")
    print("0 - Retornar")

    opcao = self.le numofae
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_aeronave(self):
    print("-------- DADOS aeronave ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    return {"nome": nome, "telefone": telefone, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_aeronave(self, dados_aeronave):
    print("NOME DO aeronave: ", dados_aeronave["nome"])
    print("FONE DO aeronave: ", dados_aeronave["telefone"])
    print("CPF DO aeronave: ", dados_aeronave["cpf"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_aeronave(self):
    cpf = input("CPF do aeronave que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)