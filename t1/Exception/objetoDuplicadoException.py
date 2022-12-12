class ObjetoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("O objeto duplicado!")
