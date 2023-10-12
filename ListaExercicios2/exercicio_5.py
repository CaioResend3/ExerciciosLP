class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saque não permitido. Verifique o valor ou saldo disponível.")

    def mostrarInformacoes(self):
        print("Número da Conta:", self.numero_conta)
        print("Nome do Correntista:", self.nome_correntista)
        print("Saldo:", self.saldo)

minha_conta = ContaCorrente(numero_conta="12345", nome_correntista="João")
minha_conta.mostrarInformacoes()
minha_conta.deposito(1000)
minha_conta.saque(500)

print("\nApós algumas operações:")
minha_conta.mostrarInformacoes()