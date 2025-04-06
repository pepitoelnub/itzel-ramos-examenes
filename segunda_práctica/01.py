class Empleado:
    """Atributos"""
    nombre = "Itzel"
    edad = 17
    sueldo = 1000
    nacionalidad = "peruano"

    """Constructor"""
    def __init__(self, nombre, edad, sueldo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = nacionalidad

    """Métodos"""
    def nombre(self):
        self.nombre = input("Nombre: ")

    def edad(self):
        self.edad = input("Edad: ")

    def cumpleaños(self):
        self.edad += 1

    def aumentoSueldo(self):
        self.sueldo = self.sueldo + self.sueldo*0.30

    def edadfutura(self, año, edad_2):
        if edad_2 < self.edad:
            return "No es posible realizar la operación"
        else:
            return f"En el año {año} tendrá {edad_2} años."

"""Instancia"""
empleado_01 = Empleado("Juan", 30, 500, "peruano")
empleado_02 = Empleado("Victor", 24, 800, "peruano")

print(empleado_01.edadfutura(2024, 50))
print(empleado_02.edadfutura(2024, 22))





