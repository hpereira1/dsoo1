from DAOs.dao import DAO
from Entidade.funcionario import Funcionario

#cada entidade terá uma classe dessa, implementação bem simples.
class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if((funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.id, str)):
            super().add(funcionario.id, funcionario)

    def update(self, funcionario: Funcionario):
        if((funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.id, str)):
            super().update(funcionario.id, funcionario)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)