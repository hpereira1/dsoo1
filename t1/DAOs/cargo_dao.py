from DAOs.dao import DAO
from Entidade.cargo import Cargo

#cada entidade terá uma classe dessa, implementação bem simples.
class CargoDAO(DAO):
    def __init__(self):
        super().__init__('cargos.pkl')

    def add(self, cargo: Cargo):
        if((cargo is not None) and isinstance(cargo, Cargo) and isinstance(cargo.id, str)):
            super().add(cargo.id, cargo)

    def update(self, cargo: Cargo):
        if((cargo is not None) and isinstance(cargo, Cargo) and isinstance(cargo.id, str)):
            super().update(cargo.id, cargo)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)