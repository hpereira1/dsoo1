from Limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaAeronave(TelaAbstrata):
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
      [sg.Text('-------- AERONAVES ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir aeronave', "RD1", key='1')],
      [sg.Radio('Alterar aeronave', "RD1", key='2')],
      [sg.Radio('Listar aeronaves', "RD1", key='3')],
      [sg.Radio('Excluir aeronave', "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
     
    ]
    self.__window = sg.Window('Sistema cia. aerea').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def pega_dados_aeronave(self):
    sg.ChangeLookAndFeel('DarkBlue')
    layout = [
      [sg.Text('-------- DADOS aeronave ----------', font=("Helvica", 25))],
      [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
      [sg.Text('Modelo:', size=(15, 1)), sg.InputText('', key='modelo')],
      [sg.Text('Combustível:', size=(15, 1)), sg.InputText('', key='combustivel')],
      [sg.Text('Numero maximo passageiros:', size=(15, 1)), sg.InputText('', key='numero_max_passageiros')],
      [sg.Text('Peso maximo decolagem:', size=(15, 1)), sg.InputText('', key='peso_max_decolagem')],
      [sg.Text('Distancia maxima:', size=(15, 1)), sg.InputText('', key='distancia_maxima')],
      [sg.Text('Numero minimo tripulantes:', size=(15, 1)), sg.InputText('', key='numero_min_tripulantes')],
      #[sg.Text('Status:', size=(15, 1)), sg.InputText('', key='status')],
         
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema aeronaves').Layout(layout)

    button, values = self.open()
    codigo = values['codigo']
    modelo = values['modelo']
    combustivel = values['combustivel']
    numero_max_passageiros = values['numero_max_passageiros']
    peso_max_decolagem = values['peso_max_decolagem']
    distancia_maxima = values['distancia_maxima']
    numero_min_tripulantes = values["numero_min_tripulantes"]
    #status = values["status"]
    
    

    self.close()
    return {"codigo": codigo, "modelo": modelo, "combustivel": combustivel, "numero_max_passageiros":numero_max_passageiros,
            "peso_max_decolagem": peso_max_decolagem, "distancia_maxima": distancia_maxima, "numero_min_tripulantes":numero_min_tripulantes,
            #"status":status 
            
            }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_aeronave(self, dados_aeronave):
    str_todas_aeronaves = ""
    #str_teste = ""
    for dado in dados_aeronave:
      str_todas_aeronaves = str_todas_aeronaves + "Codigo da aeronave: " + str(dado["codigo"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Modelo da aeronave: " + str(dado["modelo"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Combustivel da aeronave: " + str(dado["combustivel"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Numero max. passageiros da aeronave: " + str(dado["numero_max_passageiros"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Peso max. decolagem: " + str(dado["peso_max_decolagem"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Distancia maxima: " + str(dado["distancia_maxima"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Numero min. tripulantes: " + str(dado["numero_min_tripulantes"]) + '\n'
      str_todas_aeronaves = str_todas_aeronaves + "Status: " + dado["status"] + '\n\n'  
    
      #sg.Popup('-------- LISTA DE AERONAVES ----------', str_todas_aeronaves)
    col1=[[sg.Text(str_todas_aeronaves)]]
    #dado1 = str_todas_aeronaves
    #str_teste = str_teste + dados_aeronave[0].codigo()   
    layout = [     
      [sg.Text(str_todas_aeronaves)]
     
              
      #[sg.Column(col1,scrollable=True)]
          
      
    ]
    self.__window = sg.Window('Lista aeronave').Layout(layout)
    values = self.open()
    

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_aeronave(self):
    sg.ChangeLookAndFeel('DarkBlue')
    layout = [
      [sg.Text('-------- SELECIONAR aeronave ----------', font=("Helvica", 25))],
      [sg.Text('Digite o CODIGO do aeronave que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona aeronave').Layout(layout)

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
  
  
  
  
  
  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # tela_sistema = TelaAbstrata()
  # def tela_opcoes(self):
  #   print("-------- Aeronaves ----------")
  #   print("Escolha a opcao")
  #   print("1 - Incluir aeronave")
  #   print("2 - Alterar aeronave")
  #   print("3 - Listar aeronaves")
  #   print("4 - Excluir aeronave")
  #   #print("5 - Historico aeronave")
  #   print("0 - Retornar")

    
  #   opcao = self.tela_sistema.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4])
    
  #   return opcao

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def pega_dados_aeronave(self):
  #   print("-------- DADOS aeronave ----------")
  #   codigo = input("Codigo: ")
  #   modelo = input("Modelo: ")
  #   combustivel = self.tela_sistema.le_num_inteiro("Combustivel (kg): ")
  #   numero_max_passageiros = self.tela_sistema.le_num_inteiro("Numero maximo passageiros: ")
  #   peso_max_decolagem = self.tela_sistema.le_num_inteiro("Peso maximo decolagem (kg): ")
  #   distancia_maxima = self.tela_sistema.le_num_inteiro("Distancia maxima (km): ")
  #   numero_min_tripulantes = self.tela_sistema.le_num_inteiro("Numero minimo tripulantes: ")
  #   #combustivel = input("Combustivel (kg): ")
  #   #self.tela_sistema.sao_numeros(combustivel)
  #   #numero_max_passageiros = input("Numero maximo de passageiros: ")    
  #   #peso_max_decolagem = input("Peso maximo de decolagem (kg): ")
  #   #distancia_maxima = input("Distancia maxima (km): ")
  #   #numero_min_tripulantes = input("Numero minimo de tripulantes: ")
    
  #   return {"codigo": codigo, "modelo": modelo, 
  #           "combustivel":combustivel, "numero_max_passageiros": numero_max_passageiros, 
  #           "peso_max_decolagem": peso_max_decolagem, "distancia_maxima":distancia_maxima, "numero_min_tripulantes":numero_min_tripulantes
  #           }

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def mostra_aeronave(self, dados_aeronave):
  #   print("Codigo da aeronave: ", dados_aeronave["codigo"])
  #   print("Modelo da aeronave: ", dados_aeronave["modelo"])
  #   print("Combustivel da aeronave: ", dados_aeronave["combustivel"])
  #   print("Numero maximo de passageiros: ", dados_aeronave["numero_max_passageiros"])
  #   print("Peso maximo de decolagem: ", dados_aeronave["peso_max_decolagem"])
  #   print("Distancia maxima: ", dados_aeronave["distancia_maxima"])
  #   print("Numero minimo de tripulantes: ", dados_aeronave["numero_min_tripulantes"])
   
  #   print("\n")
    
  # def entrada(self,arg):
  #     print(arg)
  #     entrada = input("> ")
  #     return entrada

  # # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def seleciona_aeronave(self):
  #   codigo = input("Codigo do aeronave que deseja selecionar: ")
  #   return codigo

  # def mostra_mensagem(self, msg):
  #   print(msg)