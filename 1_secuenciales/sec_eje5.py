print("")
print("Guía de Ejercicios Secuenciales - Ejercicio 5")
print("--"*30)
print("--"*30)
print("------------Carga de Datos------------")
print("")

dolar_oficial = float(input("DOLAR OFICIAL: A cuanto cotiza el dolar oficial?: ")) # 1 Dolar Oficial a 920 pesos arg
dolar_blue = float(input("DOLAR BLUE: A cuanto cotiza el dolar blue?: ")) # 1 Dolar Blue a 1220 pesos arg
real = float(input("BRASIL: A cuanto cotiza el Peso Real?: ")) # 1 Real Blue a 215 pesos arg
pesoch = float(input("CHILE: A cuanto cotiza el Peso Chileno?: ")) # 1 Peso Ch Blue a 1.3 pesos arg
pesouy = float(input("URUGUAY: A cuanto cotiza el Peso Uruguayo?: ")) # 1 Peso Uy Blue a 25 pesos arg
print("")

pesos=int(input("Ingrese cantidad de pesos argentinos para convertir a 4 monedas extranjeras: "))
print("")

oficial = round((pesos / dolar_oficial),2)
blue = round((pesos / dolar_blue),2)
realblue = round(pesos / real)
pesochblue = round(pesos / pesoch)
pesouyblue = round(pesos / pesouy)

print("")

print("----------------Salida----------------")
print("")
print(f"La cantidad de $ {pesos}, equivale a U$D {oficial}, a un Dolar Oficial de --> U$D {dolar_oficial}")
print(f"La cantidad de $ {pesos}, equivale a U$D {blue}, a un Dolar Blue de --> U$D {dolar_blue}")
print("")
print(f"La cantidad de $ {pesos}, equivale a $ {realblue} Reales. Un Real Blue a --> $ {real}")
print("")
print(f"La cantidad de $ {pesos}, equivale a $ {pesochblue} Chilenos. Un Chileno Blue a --> $ {pesoch}")
print("")
print(f"La cantidad de $ {pesos}, equivale a $ {pesouyblue} Uruguayos. Un Uruguayo Blue a --> $ {pesouy}")

print("--"*30)
print("--"*30)

