from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []
    
    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos
    
    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        incluido_cliente = 0
        for i in self.__clientes:
            if i.codigo == codigo:
                incluido_cliente = 1
        if not incluido_cliente:
            cliente_novo = Cliente(nome, codigo)
            self.__clientes.append(cliente_novo)
            return cliente_novo
    
    def inclui_tecnico(self, codigo: int, nome:str) -> Tecnico:
        incluido_tecnico = 0
        for i in self.__tecnicos:
            if i.codigo == codigo:
                incluido_tecnico = 1
        if not incluido_tecnico:
            tecnico_novo = Tecnico(nome, codigo)
            self.__tecnicos.append(tecnico_novo)
            return tecnico_novo