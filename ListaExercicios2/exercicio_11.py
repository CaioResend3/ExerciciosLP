class Carro:
    def __init__(self, consumo_kmpl):
        self.consumo_kmpl = consumo_kmpl
        self.nivel_combustivel = 0

    def andar(self, distancia_km):
        consumo = distancia_km / self.consumo_kmpl
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
        else:
            print("Nível de combustível insuficiente para percorrer a distância especificada.")

    def obterGasolina(self):
        return self.nivel_combustivel

    def adicionarGasolina(self, litros):
        self.nivel_combustivel += litros


meuFusca = Carro(15)  

meuFusca.adicionarGasolina(20)  
meuFusca.andar(100)  

print("Combustível restante no tanque:", meuFusca.obterGasolina(), "litros")