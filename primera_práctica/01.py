nombre = "Itzel"
salario = 100
edad = "17"
universidad = "San Marcos"
apellido = "Ramos"

print(type(nombre))
print(type(salario))
print(type(edad))
print(type(universidad))
print(type(apellido))

edad = int(edad)
if edad > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    abono_final = (salario ** 2) + (salario * 10 / 100)
    print(int(abono_final))
else:
    print("Usted tiene un bono del 5% en el mes diciembre.")
    abono_final = (salario ** 2) + (salario * 5 / 100)
    print(int(abono_final))

