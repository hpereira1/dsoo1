from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, tamanho_passo = 2, volume_som = 2):
        super().__init__(tamanho_passo, volume_som)
        
    def miar(self):
        return "MAMIFERO: PRODUZ SOM: " + str(self.volume_som) + " SOM: MIAU"
