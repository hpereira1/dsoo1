class ObjetoNaoExisteException(Exception):
    def __init__(self):
        super().__init__("O objeto nao existe!")
