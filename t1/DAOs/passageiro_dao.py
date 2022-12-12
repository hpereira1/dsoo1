from DAOs.dao import DAO
from Entidade.passageiro import Passageiro

#cada entidade terá uma classe dessa, implementação bem simples.
class PassageiroDAO(DAO):
    def __init__(self):
        super().__init__('passageiros.pkl')

    def add(self, passageiro: Passageiro):
        if((passageiro is not None) and isinstance(passageiro, Passageiro) and isinstance(passageiro.id, str)):
            super().add(passageiro.id, passageiro)

    def update(self, passageiro: Passageiro):
        if((passageiro is not None) and isinstance(passageiro, Passageiro) and isinstance(passageiro.id, str)):
            super().update(passageiro.id, passageiro)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)