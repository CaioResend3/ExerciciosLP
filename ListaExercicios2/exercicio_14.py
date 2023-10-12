class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        if porcentualDeAumento > 0:
            aumento = self.salario * (porcentualDeAumento / 100)
            self.salario += aumento

caio = Funcionario("Caio", 25000)
print("Salário inicial de Caio:", caio.obterSalario())

caio.aumentarSalario(10)
print("Salário após aumento de 10%:", caio.obterSalario())