""""
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo
"""
import random


def num_aleatorios():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista generada:")
    print(lista)
    return lista


def num_no_repetidos(lista):
    new_list = list(set(lista))
    print("Lista sin repeticiones:")
    print(new_list)
    return new_list


def ordenar(lista):
    mayor_menor = sorted(lista, reverse=True)
    menor_mayor = sorted(lista)
    print("Lista ordenada de mayor a menor: {}".format(mayor_menor))
    print("Lista ordenada de menor a mayor: {}".format(menor_mayor))
    return mayor_menor, menor_mayor


def par_mayor(lista):
    pares = [num for num in lista if num % 2 == 0]
    if pares:
        mayor_par = max(pares)
        print("El par mayor de la lista es: {}".format(mayor_par))
        return mayor_par
    else:
        print("No hay pares")
        return None
