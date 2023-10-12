class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        if self.quantidade_combustivel <= 0:
            print("Desculpe, a bomba está vazia.")
            return

        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
            valor_abastecido = litros_abastecidos * self.valor_litro

        self.quantidade_combustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecer_por_litro(self, litros_abastecidos):
        if self.quantidade_combustivel < litros_abastecidos:
            print("Desculpe, a bomba não possui combustível suficiente.")
            return 0

        valor_a_pagar = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return valor_a_pagar

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

    def mostrar_estado(self):
        print(f"Tipo de Combustível: {self.tipo_combustivel}")
        print(f"Valor por Litro: R$ {self.valor_litro:.2f}")
        print(f"Quantidade de Combustível: {self.quantidade_combustivel:.2f} litros")

bomba = BombaCombustivel("Gasolina", 5.0, 1000.0)

bomba.mostrar_estado()

litros_abastecidos = bomba.abastecer_por_valor(50.0)
print(f"\nForam abastecidos {litros_abastecidos:.2f} litros.")
bomba.mostrar_estado()

valor_a_pagar = bomba.abastecer_por_litro(20.0)
print(f"\nValor a pagar: R$ {valor_a_pagar:.2f}")
bomba.mostrar_estado()

bomba.alterar_valor(5.5)
bomba.alterar_combustivel("Álcool")
bomba.alterar_quantidade_combustivel(1500.0)

print("\nApós alterações:")
bomba.mostrar_estado()