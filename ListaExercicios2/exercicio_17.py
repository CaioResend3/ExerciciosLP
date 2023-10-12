import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

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

    def __str__(self):
        return f"{self.nome}: Fome={self.fome}, Tédio={self.tedio}"

fazenda = []

num_bichinhos = int(input("Quantos bichinhos na fazenda? "))
for i in range(num_bichinhos):
    nome = input(f"Nome do bichinho {i + 1}: ")
    fazenda.append(BichinhoVirtual(nome))

while True:
    print("\nMenu:")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Passar o tempo para todos os bichinhos")
    print("4. Ouvir todos os bichinhos")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        quantidade_comida = int(input("Quanta comida você quer dar a todos os bichinhos? "))
        for bichinho in fazenda:
            bichinho.alimentar(quantidade_comida)
    elif escolha == "2":
        tempo_brincadeira = int(input("Quanto tempo você quer brincar com todos os bichinhos? "))
        for bichinho in fazenda:
            bichinho.brincar(tempo_brincadeira)
    elif escolha == "3":
        for bichinho in fazenda:
            bichinho.passarTempo(1)
    elif escolha == "4":
        for bichinho in fazenda:
            bichinho.mostrarEstado()
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")