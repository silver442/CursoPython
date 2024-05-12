import math

print("Este programa halla la raíz cuadrada de un valor numérico")

numero=int(input("Introduce un número: "))

intentos=1

while numero<0:
    
    print("El valor númerico no puede ser negativo")

    numero=int(input("Introduce un número: "))

    intentos=intentos+1

    if intentos==5:

        break

if intentos==5:
    print("Lo siento no puedo realizar el calculo")
else:
    print(math.isqrt(numero))

