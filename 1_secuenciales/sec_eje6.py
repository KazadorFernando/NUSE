print("")
print("Guía de Ejercicios Secuenciales - Ejercicio 6")
print("--"*30)
print("--"*30)
print("------------Carga de Datos------------")
print("")

precio_art=float(input("Ingrese el Precio del Artículo: "))

print("")

desc20 = round(((20 * precio_art)/100),2)
precio_final = precio_art - desc20

print("----------------Salida----------------")
print("")
print(f"Precio del Artículo $ {precio_art}. Descuento $ {desc20}. Importe Final a Pagar --> {precio_final}")

print("--"*30)
print("--"*30)

