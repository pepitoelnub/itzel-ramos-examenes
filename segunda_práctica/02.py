class Persona:
    """Atributos"""
    nombre = "Itzel"
    edad = 17
    sueldo = 1000
    nacionalidad = "peruano"
    saldo = 1000

    """Constructor"""
    def __init__(self, nombre, edad, sueldo, nacionalidad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    """Métodos"""
    def solicita_nombre(self):
        self.nombre = input("Nombre: ")

    def solicita_edad(self):
        self.edad = input("Edad: ")

    def cumpleaños(self):
        self.edad = self.edad + 1

    def aumentoSueldo(self):
        self.sueldo = self.sueldo + self.sueldo*0.30

    def edadfutura(self, año, edad_2):
        if edad_2 < self.edad:
            return "No es posible realizar la operación"
        else:
            return f"En el año {año} tendrá {edad_2} años."

    def mostrar_saldo(self):
        print("El saldo es: ", self.saldo)

    def transferencia(self, cantidad_monto, destinatario):
        if self.saldo >= cantidad_monto:
            self.saldo = self.saldo - cantidad_monto
            destinatario.saldo = destinatario.saldo + cantidad_monto
            print(f"La transferencia fue de {cantidad_monto} hacia {destinatario.nombre}")
        elif self.saldo < cantidad_monto:
            print("Saldo insuficiente")


"""Instancia"""
empleado_01 = Persona("Juan", 30, 500, "peruano", 1000)
empleado_02 = Persona("Victor", 24, 800, "peruano", 700)

empleado_01.transferencia(400, empleado_02)
"""-----------------------------------------------------------------------------"""

