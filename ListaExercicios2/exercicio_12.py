class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicioneJuros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

    def obterSaldo(self):
        return self.saldo

poupanca = ContaInvestimento(saldo_inicial=1000.00, taxa_juros=10)

for _ in range(5):
    poupanca.adicioneJuros()

saldo_final = poupanca.obterSaldo()
print("Saldo final após aplicar juros cinco vezes:", saldo_final)