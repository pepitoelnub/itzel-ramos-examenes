class Billetera:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares
        self.cambio = 3.66

    def saldo(self):
        print(f"{self.nombre} {self.apellido} - Saldo en soles: S/ {self.saldo_soles}")
        print(f"{self.nombre} {self.apellido} - Saldo en dólares: $ {self.saldo_dolares}")

    def transferir(self, cantidad, de_moneda, a_moneda):
        if de_moneda == 'soles' and a_moneda == 'dolares':
            if self.saldo_soles >= cantidad:
                cantidad_convertida = cantidad / self.cambio
                self.saldo_soles -= cantidad
                self.saldo_dolares += cantidad_convertida
                print(f"Transferencia de S/ {cantidad} a dólares realizada.")
            else:
                print("Saldo insuficiente en soles para la transferencia.")
        elif de_moneda == 'dolares' and a_moneda == 'soles':
            if self.saldo_dolares >= cantidad:
                cantidad_convertida = cantidad * self.cambio
                self.saldo_dolares -= cantidad
                self.saldo_soles += cantidad_convertida
                print(f"Transferencia de $ {cantidad} a soles realizada.")
            else:
                print("Saldo insuficiente en dólares para la transferencia.")
        self.saldo()

    def retirar(self, cantidad, moneda):
        if moneda == 'soles':
            if self.saldo_soles >= cantidad:
                self.saldo_soles -= cantidad
                print(f"Retiro de S/ {cantidad} realizado con éxito.")
            else:
                print("Saldo insuficiente en soles.")
        elif moneda == 'dolares':
            if self.saldo_dolares >= cantidad:
                self.saldo_dolares -= cantidad
                print(f"Retiro de $ {cantidad} realizado con éxito.")
            else:
                print("Saldo insuficiente.")
        self.saldo()



billetera1 = Billetera("Itzel", "Ramos", 1000, 300)
billetera2 = Billetera("Antony", "González", 900, 200)
billetera3 = Billetera("Juan", "Martínez", 500, 150)


billetera1.transferir(500, 'soles', 'dolares')
billetera2.transferir(50, 'dolares', 'soles')
billetera3.transferir(200, 'soles', 'dolares')


