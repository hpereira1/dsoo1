from Limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaVoo(TelaAbstrata):
    def __init__(self):
      super().__init__()
      self.__window = None
      self.init_opcoes()
  
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
        [sg.Text('-------- VOOS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir voo', "RD1", key='1')],
        [sg.Radio('Alterar voo', "RD1", key='2')],
        [sg.Radio('Listar voos', "RD1", key='3')],
        [sg.Radio('Excluir voo', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
      
      ]
      self.__window = sg.Window('Sistema cia aerea').Layout(layout)
     

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_voo(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- DADOS voo ----------', font=("Helvica", 25))],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
      
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Sistema voos').Layout(layout)

      button, values = self.open()
      id = values['id']
      data = values['data']
      
    

      self.close()
      return {"id": id, "data": data, 
              
              }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_voo(self, dados_voo):
      str_todas_voos = ""
      for dado in dados_voo:
        str_todas_voos = str_todas_voos + "ID do voo: " + str(dado["id"]) + '\n'
        str_todas_voos = str_todas_voos + "Data do voo: " + str(dado["data"]) + '\n'
        str_todas_voos = str_todas_voos + "Plano de voo: " + str(dado["plano_de_voo"]) + '\n'
        str_todas_voos = str_todas_voos + "Passageiros do voo: " + str(dado["passageiros_voo"]) + '\n'
        str_todas_voos = str_todas_voos + "Tripulação do voo: " + str(dado["tripulantes_voo"]) + '\n\n'
       
        
    

      sg.Popup('-------- LISTA DE VOOS ----------', str_todas_voos)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_voo(self):
      sg.ChangeLookAndFeel('DarkBlue')
      layout = [
        [sg.Text('-------- SELECIONAR voo ----------', font=("Helvica", 25))],
        [sg.Text('Digite o ID do voo que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Seleciona voo').Layout(layout)

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

    def open(self):
      button, values = self.__window.Read()
      return button, values
  
  
  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # tela_sistema = TelaAbstrata()
  # def tela_opcoes(self):
  #   print("-------- Voos ----------")
  #   print("Escolha a opcao\n")
   
    
  #   print("1 - Incluir voo")       
  #   print("2 - Alterar voo")
  #   print("3 - Listar voos")
  #   print("4 - Excluir voo")
  #   print("5 - Listar planos de voo")
  #   print("0 - Retornar")

    
  #   opcao = self.tela_sistema.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
    
  #   return opcao
  
  # def entrada(self,arg):
  #   print(arg)
  #   entrada = input(">")
    
  #   return entrada
  
  
  
    

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def pega_dados_voo(self):
  #   print("-------- DADOS VOO ----------\n")
    
  #   id = input("ID: ")
  #   data = input("Data: ")
    
     
  #   return {"id": id, "data": data, 
            
  #           }

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def mostra_voo(self, dados_voo):
  #   print("ID DO VOO: ", dados_voo["id"])
  #   print("DATA DO VOO: ", dados_voo["data"])
  #   print("PLANO DE VOO: ", dados_voo["plano_de_voo"])
  #   print("lista passageiros: ", dados_voo["passageiros_voo"])
  #   print("lista tripulacao: ", dados_voo["tripulantes_voo"])
    
  #   print("\n")




  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def seleciona_voo(self):
  #   id = input("ID do voo que deseja selecionar: ")
  #   return id


  # def mostra_mensagem(self, msg):
  #   print(msg)