from Limite.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    
    
    
    

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
    tela_sistema = TelaAbstrata()
    def tela_opcoes(self):
        print("-------- CIA AEREA ---------")
        print("Escolha sua opcao")
        print("1 - Aeronaves")
        print("2 - Voos")
        print("3 - Planos De voo")
        print("4 - Funcionarios")
        print("5 - Passageiros")        
        print("0 - Finalizar sistema")
        
        
        opcao = self.tela_sistema.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
        return opcao

