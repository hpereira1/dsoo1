from ave import Ave

class Canarinho(Ave):
    def __init__(self, altura_voo: int, tamanho_passo: int):
        super().__init__(altura_voo, tamanho_passo)

    def cantar(self):
        return "AVE: PRODUZ SOM: PIU"
    