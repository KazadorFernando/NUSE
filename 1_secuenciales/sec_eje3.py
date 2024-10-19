print("")
print("Guía de Ejercicios Secuenciales - Ejercicio 3")
print("--"*30)
print("--"*30)
print("------------Carga de Datos------------")
print("")

base=int(input("Ingrese la Base del rectángulo: "))
altura=int(input("Ingrese la Altura del rectángulo: "))
radio=int(input("Ingrese el Radio de la circunferencia: "))
print("")

import math

area_rec = (base * altura)
area_circ = round(math.pi * (radio ** 2),2)


print("----------------Salida----------------")
print("")
print(f"Área del Rectángulo --> Base: {base} * Altura: {altura} es --> {area_rec}")
print(f"Área de la Circunferencia --> Pi: {round(math.pi,2)} * Radio: {radio} ^ 2 --> {area_circ}")

print("--"*30)
print("--"*30)

