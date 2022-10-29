from Limite.tela_abstrata import TelaAbstrata

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

    opcao = self.le_num_inteiro()
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_passageiro(self):
    print("-------- DADOS passageiro ----------")
    try:
      nome = input("Nome: ")
      id = input("ID: ")
      email = input("Email: ")
      return {"nome": nome, "id": id, "email": email}
    except TypeError:
      self.mostra_mensagem("typeError")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_passageiro(self, dados_passageiro):
    print("NOME DO passageiro: ", dados_passageiro["nome"])
    print("ID DO passageiro: ", dados_passageiro["id"])
    print("EMAIL DO passageiro: ", dados_passageiro["email"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_passageiro(self):
    id_passageiro = input("ID do passageiro que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)