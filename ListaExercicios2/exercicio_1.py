class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

minha_bola = Bola(cor="amarelo", circunferencia=20, material="metal")

print("Cor da bola:", minha_bola.mostraCor())

minha_bola.trocaCor("vermelho")
print("Nova cor da bola:", minha_bola.mostraCor())
