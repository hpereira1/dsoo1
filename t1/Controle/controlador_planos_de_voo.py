from Limite.tela_plano_de_voo import TelaPlanoDeVoo
from Entidade.plano_de_voo import PlanoDeVoo


class ControladorPlanosDeVoo():


    def __init__(self, controlador_sistema):
        self.__planos_de_voo = []
        self.__tela_plano_de_voo = TelaPlanoDeVoo()
        self.__controlador_sistema = controlador_sistema
        
    
    def pega_plano_de_voo_por_codigo(self, codigo: str):
        for plano_de_voo in self.__planos_de_voo:
            if(plano_de_voo.codigo == codigo):
                return plano_de_voo
        return None
    
    def incluir_plano_de_voo(self, id_voo:str):
        dados_plano_de_voo = self.__tela_plano_de_voo.pega_dados_plano_de_voo()
        plano_de_voo = self.pega_plano_de_voo_por_codigo(dados_plano_de_voo["codigo"])
        try:
            if plano_de_voo == None:
                plano_de_voo = PlanoDeVoo(
                    dados_plano_de_voo["id_voo"],
                    dados_plano_de_voo["codigo"], dados_plano_de_voo["distancia"],dados_plano_de_voo["numero_passageiros"],dados_plano_de_voo["peso"],
                    dados_plano_de_voo["aeronave"]  
                )
                self.__planos_de_voo.append(plano_de_voo)
                voo1 = self.__controlador_sistema.controlador_voo.pega_voo_por_id(id_voo)
                print(voo1.id)
                #self.__controlador_sistema.controlador_voo.voo.plano_de_voo = plano_de_voo 
               
            else:
                raise KeyError
        except KeyError:
            self.__tela_plano_de_voo.mostra_mensagem("Plano de voo já existente!")
    
    def alterar_plano_de_voo(self):
        self.lista_planos_de_voos()
        codigo_plano_de_voo = self.__tela_plano_de_voo.seleciona_plano_de_voo()
        plano_de_voo = self.pega_plano_de_voo_por_codigo(codigo_plano_de_voo)
    
        if(plano_de_voo is not None):
            novos_dados_plano_de_voo = self.__tela_plano_de_voo.pega_dados_plano_de_voo()
            plano_de_voo.codigo = novos_dados_plano_de_voo["codigo"]
            plano_de_voo.distancia = novos_dados_plano_de_voo["distancia"]
            plano_de_voo.numero_passageiros = novos_dados_plano_de_voo["numero_passageiros"]
            plano_de_voo.peso = novos_dados_plano_de_voo["peso"]
            plano_de_voo.aeronave = novos_dados_plano_de_voo["aeronave"]     
        
            self.lista_planos_de_voos()
        else:
            self.__tela_plano_de_voo.mostra_mensagem("ATENCAO: plano_de_voo não existente")

  # # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_planos_de_voos(self):        
        try:
            if not self.__planos_de_voo:
                raise Exception                
        except Exception:
            self.__tela_plano_de_voo.mostra_mensagem("\nNENHUM PLANO DE VOO ENCONTRADO!\n")
            
        for plano_de_voo in self.__planos_de_voo:
                self.__tela_plano_de_voo.mostra_plano_de_voo({"codigo": plano_de_voo.codigo, "distancia": plano_de_voo.distancia,
                                                            "numero_passageiros":plano_de_voo.numero_passageiros,"peso":plano_de_voo.peso,"aeronave":plano_de_voo.aeronave                                                            
                                                        })    

    def excluir_plano_de_voo(self):
        self.lista_planos_de_voos()
        codigo_plano_de_voo = self.__tela_plano_de_voo.seleciona_plano_de_voo()
        plano_de_voo = self.pega_plano_de_voo_por_codigo(codigo_plano_de_voo)

        if(plano_de_voo is not None):
            self.__planos_de_voo.remove(plano_de_voo)
            self.lista_planos_de_voos()
        else:
            self.__tela_plano_de_voo.mostra_mensagem("ATENCAO: plano_de_voo não existente")

    def retornar(self):
        self.__controlador_sistema.controlador_voo.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_plano_de_voo, 2: self.alterar_plano_de_voo, 3: self.lista_planos_de_voos, 4: self.excluir_plano_de_voo, 0: self.retornar}   
    
        continua = True
        while continua:
            lista_opcoes[self.__tela_plano_de_voo.tela_opcoes()]()
            