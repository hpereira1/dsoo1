from Limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # precisa chamar self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de janelas depois de fechadas.
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0        
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
            [sg.Text('Gerenciador de cia. aérea. Bem vindo!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Aeronaves',"RD1", key='1')],
            [sg.Radio('Voos',"RD1", key='2')],
            [sg.Radio('Passageiros',"RD1", key='3')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
           
            
           
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
        
    
    
    

    # def le_num_inteiro(self, mensagem=" ", ints_validos = None):
    #     while True:
    #         valor_lido = input(mensagem)
    #         try:
    #             valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
    #             if ints_validos and valor_int not in ints_validos:
    #                 raise ValueError #será lançada apenas se o número não é o esperado
    #             return valor_int
    #         except ValueError: #aqui cai se não for int ou se não for valido
    #             print("Valor incorreto!")
    #             if ints_validos:
    #                 print("Valores válidos: ", ints_validos)
    # tela_sistema = TelaAbstrata()
    # def tela_opcoes(self):
    #     print("-------- CIA AEREA ---------")
    #     print("Escolha sua opcao")
    #     print("1 - Aeronaves")
    #     print("2 - Voos")        
    #     print("3 - Passageiros")
    #     print("4 - Funcionarios")        
    #     print("0 - Finalizar sistema")
        
        
    #     opcao = self.tela_sistema.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
    #     return opcao

