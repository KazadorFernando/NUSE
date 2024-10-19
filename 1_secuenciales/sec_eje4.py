print("")
print("Guía de Ejercicios Secuenciales - Ejercicio 4")
print("--"*30)
print("--"*30)
print("------------Carga de Datos------------")
print("")

dolar_oficial = float(input("DOLAR OFICIAL: A cuanto cotiza el dolar oficial?: ")) # 1 Dolar Oficial a 920 pesos arg
dolar_blue = float(input("DOLAR BLUE: A cuanto cotiza el dolar blue?: ")) # 1 Dolar Blue a 1220 pesos arg

print("")

pesos=int(input("Ingrese cantidad de pesos argentinos para convertir a 4 monedas extranjeras: "))
print("")

oficial = round((pesos / dolar_oficial),2)
blue = round((pesos / dolar_blue),2)

print("")

print("----------------Salida----------------")
print("")
print(f"La cantidad de $ {pesos}, equivale a U$D {oficial}, a un Dolar Oficial de --> U$D {dolar_oficial}")
print(f"La cantidad de $ {pesos}, equivale a U$D {blue}, a un Dolar Blue de --> U$D {dolar_blue}")


print("--"*30)
print("--"*30)

