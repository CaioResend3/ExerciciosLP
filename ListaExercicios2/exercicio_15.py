class BichinhoVirtual:
    def __init__(self, nome, fome=0, tedio=0):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira

    def passarTempo(self, tempo):
        self.fome += tempo
        self.tedio += tempo

    def humor(self):
        if self.fome > 10 or self.tedio > 10:
            return "Muito triste"
        elif self.fome > 5 or self.tedio > 5:
            return "Triste"
        else:
            return "Feliz"

    def mostrarEstado(self):
        print(f"{self.nome} está se sentindo {self.humor()}.")
        print(f"Fome: {self.fome}")
        print(f"Tédio: {self.tedio}")

bichinho = BichinhoVirtual("Fofinho")

bichinho.mostrarEstado()

quantidade_comida = int(input("Quanta comida você quer dar ao bichinho? "))
tempo_brincadeira = int(input("Quanto tempo você quer brincar com o bichinho? "))

bichinho.alimentar(quantidade_comida)
bichinho.brincar(tempo_brincadeira)

bichinho.passarTempo(1)

print("\nDepois de um tempo:")
bichinho.mostrarEstado()