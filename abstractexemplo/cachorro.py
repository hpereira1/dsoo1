from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self, tamanho_passo = 3, volume_som = 3):
        super().__init__(tamanho_passo, volume_som)
    
    def latir(self):
        som = "MAMIFERO: PRODUZ SOM: " + str(self.volume_som) + " SOM: AU"
        return som

