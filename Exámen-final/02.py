"""
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
- La función que vas a crear va a capturar, la edad, nombre de un alumnos y la
hora y el minuto en que fue registrado (usar la librería correspondiente)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""
from datetime import datetime


def conteo(func):
    def mayor_01(*args, **kwargs):
        total_args = len(args) + len(kwargs)
        if total_args < 1:
            print("Se necesita más de un parámetro para procesar.")
            return None
        resultado = func(*args, **kwargs)
        print("La función fue ejecutada.")
        return resultado
    return mayor_01


@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    hora_actual = datetime.now()
    hora = hora_actual.hour
    minuto = hora_actual.minute

    media_nota = (nota1 + nota2 + nota3 + nota4) / 4
    print("{} de {} años ha sido registrado a las {} "
          "horas con {} minutos.".format(nombre, edad, hora, minuto))
    print("Promedio del estudiante: {:.2f}".format(media_nota))
    return media_nota


registrar_alumno("Pedro", 30, 16, 19, 12, 11)
