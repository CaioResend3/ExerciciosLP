class Retangulo:
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB

    def mudarLados(self, novo_LadoA, novo_LadoB):
        self.LadoA = novo_LadoA
        self.LadoB = novo_LadoB

    def retornarLados(self):
        return self.LadoA, self.LadoB

    def calcularArea(self):
        return self.LadoA * self.LadoB

    def calcularPerimetro(self):
        return 2 * (self.LadoA + self.LadoB)

if __name__ == '__main__':
   
    LadoA = float(input("Informe a medida do Lado A do local: "))
    LadoB = float(input("Informe a medida do Lado B do local: "))

    local = Retangulo(LadoA, LadoB)

    area_local = local.calcularArea()

    perimetro_local = local.calcularPerimetro()

    quantidade_de_pisos = area_local

    medida_rodape = min(LadoA, LadoB) / 2
    quantidade_de_rodapes = perimetro_local / medida_rodape

    print(f"Área do local: {area_local} metros quadrados")
    print(f"Perímetro do local: {perimetro_local} metros")
    print(f"Quantidade de pisos necessários: {quantidade_de_pisos} pisos")
    print(f"Quantidade de rodapés necessários: {quantidade_de_rodapes} rodapés")