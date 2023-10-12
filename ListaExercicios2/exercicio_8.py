class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        print(f"Bucho de {self.nome}: {', '.join(self.bucho)}")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo {self.bucho[0]}...")
            self.bucho.pop(0)
        else:
            print(f"{self.nome} não tem nada no estômago para digerir.")

macaco1 = Macaco("Jonas")
macaco2 = Macaco("Winston")

macaco1.comer("banana")
macaco1.comer("maçã")
macaco2.comer("manga")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()

macaco2.comer("Chico")
macaco2.verBucho()