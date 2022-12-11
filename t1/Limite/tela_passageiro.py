from Limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPassageiro(TelaAbstrata):
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
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
          opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
      # sg.theme_previewer()
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- PASSAGEIROS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir passageiro', "RD1", key='1')],
        [sg.Radio('Alterar passageiro', "RD1", key='2')],
        [sg.Radio('Listar passageiros ', "RD1", key='3')],
        [sg.Radio('Excluir passageiro', "RD1", key='4')],
        [sg.Radio('Ver historico por ID', "RD1", key='5')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
      
      ]
      self.__window = sg.Window('Sistema cia aerea').Layout(layout)
     

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    '''
    def pega_dados_passageiro(self):
    print("-------- DADOS passageiro ----------")
    try:
      nome = input("Nome: ")
      id = input("ID: ")
      email = input("Email: ")
      return {"nome": nome, "id": id, "email": email}
    except TypeError:
      self.mostra_mensagem("typeError")
    '''
  
    def pega_dados_passageiro(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- DADOS passageiro ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Sistema passageiros').Layout(layout)

      button, values = self.open()
      nome = values['nome']
      id = values['id']
      email = values['email']
    
      self.close()
      return {"nome": nome,"id": id, "email": email, 
              
              }
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    ''' 
    def mostra_passageiro(self, dados_passageiro):
      print("NOME DO passageiro: ", dados_passageiro["nome"])
      print("ID DO passageiro: ", dados_passageiro["id"])
      print("EMAIL DO passageiro: ", dados_passageiro["email"])
      print("\n")
    '''
    def mostra_passageiro(self, dados_passageiro):
      str_todas_passageiros = ""
      for dado in dados_passageiro:
        str_todas_passageiros = str_todas_passageiros + "Nome do passageiro: " + str(dado["nome"]) + '\n'
        str_todas_passageiros = str_todas_passageiros + "ID do passageiro: " + str(dado["id"]) + '\n'
        str_todas_passageiros = str_todas_passageiros + "Email do passageiro: " + str(dado["email"]) + '\n\n'
       
        
    

      #sg.Popup('-------- LISTA DE Passageiros ----------', str_todas_passageiros)
    
    
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    '''
    def seleciona_passageiro(self):
      id_passageiro = input("ID do passageiro que deseja selecionar: ")
      return id_passageiro
    '''
    def seleciona_passageiro(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- SELECIONAR passageiro ----------', font=("Helvica", 25))],
        [sg.Text('Digite o ID do passageiro que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Seleciona passageiro').Layout(layout)

      button, values = self.open()
      id = values['id']
      self.close()
      return id
    
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

