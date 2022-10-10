from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from collections import defaultdict
from cliente import Cliente
from tecnico import Tecnico 


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__tipoChamados = []
        self.__chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        count = 0
        for i in self.__chamados:
            if i.tipo.codigo == tipo.codigo:
                count += 1
        return count
    
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico,titulo: str,
            descricao: str,prioridade: int,tipo: TipoChamado) -> Chamado:
        if type(cliente) is Cliente and type(tecnico) is Tecnico and type(tipo) is TipoChamado:
            chamado_incluso = 0
            for i in self.__chamados:
                if data == i.data and cliente.codigo == i.cliente.codigo and tecnico.codigo == i.tecnico.codigo and tipo.codigo == i.tipo.codigo:
                    chamado_incluso = 1
            if not chamado_incluso:
                novo = Chamado( data,cliente,tecnico,titulo,descricao,prioridade,tipo)
                self.__chamados.append(novo)
                return novo
    
    def inclui_tipochamado(self,codigo: int,nome: str,descricao: str) -> TipoChamado:
        tipo_incluso = 0
        for i in self.__tipoChamados:
            if codigo == i.codigo:
                tipo_incluso = 1
        if not tipo_incluso:
            novo = TipoChamado(codigo, descricao, nome)
            self.__tipoChamados.append(novo)
            return novo

    @property
    def tipos_chamados(self):
        return self.__tipoChamados
