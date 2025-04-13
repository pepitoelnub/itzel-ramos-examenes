import funciones01


def main():
    lista = funciones01.num_aleatorios()
    sin_repetidos = funciones01.num_no_repetidos(lista)
    funciones01.ordenar(sin_repetidos)
    funciones01.par_mayor(lista)


main()
