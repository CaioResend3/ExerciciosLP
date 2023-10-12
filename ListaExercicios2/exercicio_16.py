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

    def __str__(self):
        return f"{self.nome}: Fome={self.fome}, Tédio={self.tedio}"

bichinho = BichinhoVirtual("Fofinho")

while True:
    print("\nMenu:")
    print("1. Alimentar")
    print("2. Brincar")
    print("3. Passar o tempo")
    print("4. Mostrar estado")
    print("5. Mostrar valores exatos (secreto)")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        quantidade_comida = int(input("Quanta comida você quer dar ao bichinho? "))
        bichinho.alimentar(quantidade_comida)
    elif escolha == "2":
        tempo_brincadeira = int(input("Quanto tempo você quer brincar com o bichinho? "))
        bichinho.brincar(tempo_brincadeira)
    elif escolha == "3":
        bichinho.passarTempo(1)
    elif escolha == "4":
        bichinho.mostrarEstado()
    elif escolha == "5":
        print(bichinho)  
    elif escolha == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")