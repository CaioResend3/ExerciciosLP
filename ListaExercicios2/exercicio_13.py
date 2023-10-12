class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

funcionario1 = Funcionario("Caio", 3500.00)
funcionario2 = Funcionario("Lucas", 4200.00)

print("Nome do funcionário 1:", funcionario1.obterNome())
print("Salário do funcionário 1:", funcionario1.obterSalario())

print("Nome do funcionário 2:", funcionario2.obterNome())
print("Salário do funcionário 2:", funcionario2.obterSalario())