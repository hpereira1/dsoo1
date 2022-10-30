from Limite.tela_abstrata import TelaAbstrata

class TelaFuncionario(TelaAbstrata):
    
    
  def tela_opcoes(self):
    print("-------- funcionarios ----------")
    print("Escolha a opcao")
    print("1 - Incluir funcionario")
    print("2 - Alterar funcionario")
    print("3 - Listar funcionarios")
    print("4 - Excluir funcionario")
    print("5 - Incluir cargo")
    print("6 - Alterar cargo")
    print("7 - Listar cargo")
    print("9 - Excluir cargo")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5,6,7,8,9])
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_funcionario(self):
    print("-------- DADOS funcionario ----------")
    try:
      nome = input("Nome: ")
      id = input("ID: ")
      email = input("Email: ")
      cargo = input("Cargo: ")
      return {"nome": nome, "id": id, "email": email, "cargo": cargo}
    except TypeError:
      self.mostra_mensagem("typeError")

  def pega_dados_cargo(self):
    print("-------- DADOS cargo ----------")
    try:
      descricao = input("Descricao: ")
      id = input("ID: ")
      salario = float(input("salario: "))
      return {"descricao": descricao, "id": id, "salario": salario}
    except TypeError:
      self.mostra_mensagem("typeError")
      
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_funcionario(self, dados_funcionario):
    print("NOME DO funcionario: ", dados_funcionario["nome"])
    print("ID DO funcionario: ", dados_funcionario["id"])
    print("EMAIL DO funcionario: ", dados_funcionario["email"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_funcionario(self):
    id_funcionario = input("ID do funcionario que deseja selecionar: ")
    return id_funcionario

  def seleciona_cargo(self):
    id_cargo = input("ID do cargo que deseja selecionar: ")
    return id_cargo

  def mostra_mensagem(self, msg):
    print(msg)