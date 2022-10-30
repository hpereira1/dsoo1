class Cargo:
    def __init__(self, descricao: str, id: str, salario: float):
        self.__descricao = descricao
        self.__id = id
        self.__salario = salario
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def id(self):
        return self.__id
    
    @property
    def salario(self):
        return self.__salario
    
    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
        
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id
            
    @salario.setter
    def salario(self, salario):
        if isinstance(salario, float):
            self.__salario = salario