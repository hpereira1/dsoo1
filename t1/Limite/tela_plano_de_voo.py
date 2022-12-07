
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
    sg.ChangeLookAndFeel('DarkTeal4')
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
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS plano_de_voo ----------', font=("Helvica", 25))],
      [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
      [sg.Text('Modelo:', size=(15, 1)), sg.InputText('', key='modelo')],
      [sg.Text('Combustível:', size=(15, 1)), sg.InputText('', key='combustivel')],
      [sg.Text('Numero maximo passageiros:', size=(15, 1)), sg.InputText('', key='numero_max_passageiros')],
      [sg.Text('Peso maximo decolagem:', size=(15, 1)), sg.InputText('', key='peso_max_decolagem')],
      [sg.Text('Distancia maxima:', size=(15, 1)), sg.InputText('', key='distancia_maxima')],
      [sg.Text('Numero minimo tripulantes:', size=(15, 1)), sg.InputText('', key='numero_min_tripulantes')],
         
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema plano_de_voos').Layout(layout)

    button, values = self.open()
    codigo = values['codigo']
    modelo = values['modelo']
    combustivel = values['combustivel']
    numero_max_passageiros = values['numero_max_passageiros']
    peso_max_decolagem = values['peso_max_decolagem']
    distancia_maxima = values['distancia_maxima']
    numero_min_tripulantes = values["numero_min_tripulantes"]
    
    

    self.close()
    return {"codigo": codigo, "modelo": modelo, "combustivel": combustivel, "numero_max_passageiros":numero_max_passageiros,
            "peso_max_decolagem": peso_max_decolagem, "distancia_maxima": distancia_maxima, "numero_min_tripulantes":numero_min_tripulantes 
            
            }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_plano_de_voo(self, dados_plano_de_voo):
    str_todas_plano_de_voos = ""
    for dado in dados_plano_de_voo:
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Codigo da plano_de_voo: " + str(dado["codigo"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Modelo da plano_de_voo: " + str(dado["modelo"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Combustivel da plano_de_voo: " + str(dado["combustivel"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Numero max. passageiros da plano_de_voo: " + str(dado["numero_max_passageiros"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Peso max. decolagem: " + str(dado["peso_max_decolagem"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Distancia maxima: " + str(dado["distancia_maxima"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Numero min. tripulantes: " + str(dado["numero_min_tripulantes"]) + '\n'
      str_todas_plano_de_voos = str_todas_plano_de_voos + "Status: " + dado["status"] + '\n\n'
   

    sg.Popup('-------- LISTA DE plano_de_vooS ----------', str_todas_plano_de_voos)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_plano_de_voo(self):
    sg.ChangeLookAndFeel('DarkTeal4')
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