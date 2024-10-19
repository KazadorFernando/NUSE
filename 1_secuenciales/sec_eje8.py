print("")
print("Guía de Ejercicios Secuenciales - Ejercicio 8")
print("--"*30)
print("--"*30)
print("------------Carga de Datos------------")
print("")

anio_nac = int(input("Ingrese su Año de Nacimiento: "))
anio_act = int(input("Ingrese el Año Actual: "))
print("")

anios = (anio_act - anio_nac)
meses = (anios * 12)
semanas = (meses * 4)
dias = (semanas * 7)

print("----------------Salida----------------")
print("")
print(f"--> Año de Nacimiento: {anio_nac} - Actualmente tiene --> {anios} años.")
print(f"--> Meses vividos: {meses} meses. - Semanas vividas --> {semanas} semanas.")
print(f"--> Días vividos: {dias} días.")

print("--"*30)
print("--"*30)

