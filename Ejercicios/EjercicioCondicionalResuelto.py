print("Programa de cálculo de tipo impositivo en Renta 2020")

renta=float(input("Introduce la renta anual de esta año"))

if(renta<12000):
    tipo=7
elif(renta<18000):
    tipo=15
elif(renta<35000):
    tipo=21
elif(renta<70000):
    tipo=35
else:
    tipo=45

print("A la renta " + str(renta) + " le correspode un " + str(tipo) + "% de tipo impositivo")
