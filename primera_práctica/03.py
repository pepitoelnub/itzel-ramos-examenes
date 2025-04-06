nombre = "Itzel"
salario = 100
edad = "17"
universidad = "San Marcos"
bono = 5
apellido = "Ramos"
var_bool = True

lista_01 = [nombre, salario, edad, universidad, bono, apellido, var_bool]

hijos = True
lista_01.append(hijos)

if hijos:
    bono_familiar = salario * 8/100
    lista_01.append(bono_familiar)
    print(f"Obtiene el bono familiar el cual es de: {bono_familiar}")
    print(lista_01)
else:
    print("No cumple para obtener el bono familiar")
