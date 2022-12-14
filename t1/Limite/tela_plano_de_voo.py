
from Limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaPlanoDeVoo(TelaAbstrata):
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
      [sg.Text('-------- PLANOP DE VOO ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir plano_de_voo', "RD1", key='1')],
      [sg.Radio('Alterar plano_de_voo', "RD1", key='2')],
      [sg.Radio('Listar plano_de_voos', "RD1", key='3')],
      [sg.Radio('Excluir plano_de_voo', "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
     
    ]
    self.__window = sg.Window('Sistema cia. aerea').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def pega_dados_plano_de_voo(self):
    sg.ChangeLookAndFeel('DarkBlue')
    layout = [
      [sg.Text('-------- DADOS plano_de_voo ----------', font=("Helvica", 25))],
      [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
      [sg.Text('Distancia:', size=(15, 1)), sg.InputText('', key='distancia')],
      [sg.Text('Peso:', size=(15, 1)), sg.InputText('', key='peso')],
      
         
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema plano_de_voos').Layout(layout)

    button, values = self.open()
    codigo = values['codigo']
    distancia = values['distancia']
    peso = values['peso']

    
    

    self.close()
    return {"codigo": codigo, "distancia": distancia, "peso": peso 
            
            }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_plano_de_voo(self, dados_plano_de_voo):
    str_todas_plano_de_voos = ""
    for dado in dados_plano_de_voo:
      str_todas_plano_de_voos = str_todas_plano_de_voos + "ID do voo: " + str(dado["id_voo"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Código do Plano de Voo: " + str(dado["codigo"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Distancia do voo: " + str(dado["distancia"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Numero passageiros: " + str(dado["numero_passageiros"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Peso: " + str(dado["peso"]) + '\n\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Aeronave(modelo): " + str(dado["aeronave"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Aeronave(codigo): " + str(dado["aeronave2"]) + '\n'
      
     
   

    sg.Popup('-------- DETALHES DO PLANOS DE VOO ----------', str_todas_plano_de_voos)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_plano_de_voo(self):
    sg.ChangeLookAndFeel('DarkBlue')
    layout = [
      [sg.Text('-------- SELECIONAR plano_de_voo ----------', font=("Helvica", 25))],
      [sg.Text('Digite o CODIGO do plano_de_voo que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona plano_de_voo').Layout(layout)

    button, values = self.open()
    codigo = values['codigo']
    self.close()
    return codigo
  
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
  #   def tela_opcoes(self):
  #       print("-------- PLANOS DE VOO ----------")
  #       print("Escolha a opcao")
  #       #print("1 - Incluir Plano de Voo")
  #       print("2 - Alterar Plano de Voo")
  #       print("3 - Listar Planos de Voo")
  #       #print("4 - Excluir Plano de Voo")
  #       print("0 - Retornar")

  #       opcao = int(input("Escolha a opcao: "))
  #       return opcao

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  #   def pega_dados_plano_de_voo(self):
  #       print("-------- DADOS PLANOS DE VOO ----------")
  #       #id_voo = input("ID_VOO: ")
  #       codigo = input("CODIGO: ")
  #       distancia = input("Distancia: ")
  #       #numero_passageiros = input("Numero de passageiros: ")
  #       peso = input("Peso: ")        
  #       #plano_de_voo = input("plano_de_voo: ")

  #       return {"codigo": codigo, "distancia": distancia, 
  #               #"numero_passageiros": numero_passageiros, 
  #               "peso": peso, 
  #               #"plano_de_voo":plano_de_voo
  #                }
    
  #   def entrada(self,arg):
  #     print(arg)
  #     entrada = input("> ")
  #     return entrada

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  #   def mostra_plano_de_voo(self, dados_plano_de_voo):
  #       print("\n\n\n")
  #       print("ID do Voo: ", dados_plano_de_voo["id_voo"])
  #       print("Codigo do Plano de Voo: ", dados_plano_de_voo["codigo"])
  #       print("DISTANCIA do Voo: ", dados_plano_de_voo["distancia"])
  #       print("Numero de passageiros do Voo: ", dados_plano_de_voo["numero_passageiros"])
  #       print("Peso do Voo: ", dados_plano_de_voo["peso"])
  #       print("plano_de_voo do voo: ", dados_plano_de_voo["plano_de_voo"])
  #       print("\n")

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  #   def seleciona_plano_de_voo(self):
  #       codigo = input("CODIGO do Plano de Voo que deseja selecionar: ")
  #       return codigo

  #   def mostra_mensagem(self, msg):
  #       print(msg)