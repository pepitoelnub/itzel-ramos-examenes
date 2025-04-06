lista_01 = [ ]

nombre = "Itzel"
salario = 100
edad = "17"
universidad = "San Marcos"
bono = 5
apellido = "Ramos"

lista_01.extend([nombre, salario, edad, universidad, bono, apellido])

var_bool = True

lista_01.append(var_bool)
print(lista_01)

print("El tamaño de la lista es ", len(lista_01))

if var_bool:
    print(f"El trabajador {nombre} {apellido} se encuentra trabajando actualmente en la compañía")
else:
    print(f"El trabajador {nombre} {apellido} ya no se encuentra trabajando actualmente en la empresa")
