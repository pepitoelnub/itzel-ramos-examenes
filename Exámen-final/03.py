"""
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""
from datetime import datetime


def decorador(func):
    def funcionB(**kwargs):
        hora_actual = datetime.now()
        print("El decorador está siendo ejecutado a las {} con"
              " {} minutos".format(hora_actual.hour, hora_actual.minute))
        suma = sum(kwargs.values())
        print("La suma de los valores es: {}".format(suma))
        resultado = func(**kwargs)
        return resultado
    return funcionB


@decorador
def encontrar_mayor(**numeros):
    mayor = max(numeros.values())
    print("El mayor valor es: {}".format(mayor))
    return mayor


print("Ejemplo 1")
encontrar_mayor(n1=10, n2=25, n3=17, n4=4, n5=36, n6=12)

print("\nEjemplo 2")
encontrar_mayor(a=5, b=8, c=13, d=21, e=3)

print("\nEjemplo 3")
encontrar_mayor(x1=100, x2=98, x3=120)
