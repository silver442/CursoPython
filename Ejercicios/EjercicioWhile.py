import random

aleatorio = random.randint(1,100)
intentos=1
num = int(input("Introduce un numero entre 1 y 100: "))

while num!=aleatorio:
    if(num < aleatorio):
        print("El numero aleatorio es mayor")
    elif num > aleatorio:
        print("El numero es menor")

    num = int(input("Introduce un numero: "))
    intentos+=1

print("Correcto. Haz utilizado " + str(intentos) + " intentos")