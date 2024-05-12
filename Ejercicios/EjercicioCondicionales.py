renta = float(input("Introduce la renta: "))

if renta < 12000 :
    print("A la renta " + str(renta) + " le corresponde un 7% de tipo impositivo")
elif renta >= 12000 and renta<=18000 :
    print("A la renta " + str(renta) + " le corresponde un 15% de tipo impositivo")
elif 18000>=renta<=35000 :
    print("A la renta " + str(renta) + " le corresponde un 21% de tipo impositivo")
elif 35000>=renta<=70000 :
    print("A la renta " + str(renta) + " le corresponde un 35% de tipo impositivo")
else :
    print("A la renta " + str(renta) + " le corresponde un 45% de tipo impositivo")
