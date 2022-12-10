from Limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaFuncionario(TelaAbstrata):
    def __init__(self):
      super().__init__()
      self.__window = None
      self.init_opcoes()
      
    def open(self):
      button, values = self.__window.Read()
      return button, values
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
          opcao = 1
        if values['2']:
          opcao = 2
        if values['3']:
          opcao = 3
        if values['4']:
          opcao = 4
        if values['5']:
          opcao = 5
        if values['6']:
          opcao = 6
        if values['7']:
          opcao = 7
        if values['8']:
          opcao = 8
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
          opcao = 0
        self.close()
        return opcao

    
    '''    
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
      print("8 - Excluir cargo")
      print("0 - Retornar")

      opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5,6,7,8,9])
      return opcao
    '''
    def init_opcoes(self):
      # sg.theme_previewer()
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- FUNCIONARIOS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir funcionario', "RD1", key='1')],
        [sg.Radio('Alterar funcionario', "RD1", key='2')],
        [sg.Radio('Listar funcionarios ', "RD1", key='3')],
        [sg.Radio('Excluir funcionario', "RD1", key='4')],
        [sg.Radio('Incluir cargo', "RD1", key='5')],
        [sg.Radio('Alterar cargo', "RD1", key='6')],
        [sg.Radio('Listar cargo', "RD1", key='7')],
        [sg.Radio('Excluir cargo', "RD1", key='8')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
      
      ]
      self.__window = sg.Window('Sistema cia aerea').Layout(layout)
     

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    '''
    def pega_dados_funcionario(self):
      print("-------- DADOS funcionario ----------")
      try:
        nome = input("Nome: ")
        id = input("ID: ")
        email = input("Email: ")
        return {"nome": nome, "id": id, "email": email}
      except TypeError:
        self.mostra_mensagem("typeError")
    '''
    def pega_dados_funcionario(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- DADOS funcionario ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Sistema funcionarios').Layout(layout)

      button, values = self.open()
      nome = values['nome']
      id = values['id']
      email = values['email']
    
      self.close()
      return {"nome": nome,"id": id, "email": email, 
              
                }
    '''
    def pega_dados_cargo(self):
      print("-------- DADOS cargo ----------")
      try:
        descricao = input("Descricao: ")
        id = input("ID: ")
        salario = float(input("salario: "))
        return {"descricao": descricao, "id": id, "salario": salario}
      except TypeError:
        self.mostra_mensagem("typeError")
    '''      
    def pega_dados_cargo(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- DADOS cargo ----------', font=("Helvica", 25))],
        [sg.Text('Descricao:', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Text('Salario:', size=(15, 1)), sg.InputText('', key='salario')],
      
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Sistema funcionarios').Layout(layout)

      button, values = self.open()
      descricao = values['descricao']
      id = values['id']
      salario = values['salario']
    
      self.close()
      return {"descricao": descricao,"id": id, "salario": salario, 
              
              }
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    '''
    def mostra_funcionario(self, dados_funcionario):
      print("NOME DO funcionario: ", dados_funcionario["nome"])
      print("ID DO funcionario: ", dados_funcionario["id"])
      print("EMAIL DO funcionario: ", dados_funcionario["email"])
      print("\n")
    '''
    def mostra_funcionario(self, dados_funcionario):
      str_todas_funcionarios = ""
      for dado in dados_funcionario:
        str_todas_funcionarios = str_todas_funcionarios + "Nome do funcionario: " + str(dado["nome"]) + '\n'
        str_todas_funcionarios = str_todas_funcionarios + "ID do funcionario: " + str(dado["id"]) + '\n'
        str_todas_funcionarios = str_todas_funcionarios + "Cargo do funcionario: " + str(dado["cargo"]) + '\n'
        str_todas_funcionarios = str_todas_funcionarios + "Email do funcionario: " + str(dado["email"]) + '\n\n'
       
        
    

      sg.Popup('-------- LISTA DE funcionarios ----------', str_todas_funcionarios)
    
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    ''' 
    def seleciona_funcionario(self):
      id_funcionario = input("ID do funcionario que deseja selecionar: ")
      return id_funcionario
    '''
    def seleciona_funcionario(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- SELECIONAR funcionario ----------', font=("Helvica", 25))],
        [sg.Text('Digite o ID do funcionario que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Seleciona funcionario').Layout(layout)

      button, values = self.open()
      id = values['id']
      self.close()
      return id
  
    def seleciona_cargo(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- SELECIONAR cargo ----------', font=("Helvica", 25))],
        [sg.Text('Digite o ID do cargo que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Seleciona cargo').Layout(layout)

      button, values = self.open()
      id = values['id']
      self.close()
      return id
    '''  
    def seleciona_cargo(self):
      id_cargo = input("ID do cargo que deseja selecionar: ")
      return id_cargo
    '''
    '''  
    def mostra_mensagem(self, msg):
      print(msg)
    '''
    
    def entrada(self,arg):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [        
        [sg.Text(arg, font=("Helvica", 15))],
        [sg.InputText('', key='entrada')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        
      ]
      self.__window = sg.Window(arg).Layout(layout)
            
      button, values = self.open()
      entrada = values['entrada']
      self.close()
      return entrada  
    
    def mostra_mensagem(self, msg):
      sg.popup("", msg)
    
    def close(self):
      self.__window.Close()

