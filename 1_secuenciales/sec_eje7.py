print("")
print("Guía de Ejercicios Secuenciales - Ejercicio 7")
print("--"*30)
print("--"*30)
print("------------Carga de Datos------------")
print("")

precio_art=float(input("Ingrese el Precio del Artículo: "))

print("")

desc20 = round(((20 * precio_art)/100),2)
precio_parcial = round((precio_art - desc20),2)

iva15= round(((15 * precio_parcial)/100),2)
precio_final = round((precio_parcial + iva15),2)

print("----------------Salida----------------")
print("")
print("--> Precio del Artículo $ ", precio_art," -.")
print(f"--> Descuento 20% --> $ {desc20}. Importe Parcial a Pagar --> $ {precio_parcial}")
print(f"--> Incremento por IVA 15% --> $ {iva15}. Importe Final a Pagar --> $ {precio_final}")
print("--"*30)
print("--"*30)

