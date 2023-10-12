class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido. Informe um canal entre 1 e 100.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo atingido.")

    def mostrarStatus(self):
        print(f"Canal: {self.canal}")
        print(f"Volume: {self.volume}")

minha_tv = TV()

minha_tv.mostrarStatus()
minha_tv.mudarCanal(5)
minha_tv.aumentarVolume()
minha_tv.aumentarVolume()
minha_tv.diminuirVolume()

print("\nApós algumas operações:")
minha_tv.mostrarStatus()