class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


def main():
    ponto = Ponto(0, 0)
    retangulo = Retangulo(ponto, 4, 3)

    while True:
        print("\nMenu:")
        print("1. Imprimir valores do Ponto")
        print("2. Encontrar o centro do Retângulo")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            ponto.imprimir()
        elif escolha == "2":
            centro = retangulo.encontrarCentro()
            centro.imprimir()
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()