num1=int(input("Introduce el primer numero a empezar: "))
num2=int(input("Introduce el numero a terminar: "))

def es_primo(numero):
    for n in range(2, numero):
        if numero % n ==0:
            return False
    print(str(numero) + " es primo")
    return True

for i in range(num1,num2):
    es_primo(i)
