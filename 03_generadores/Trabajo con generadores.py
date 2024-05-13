def generarPares(limite):

    num=1

    numerosPares=[]

    while num<limite:

        yield num*2

        num=num+1
    
sucesionPares=generarPares(6)
'''
for i in sucesionPares:

    print(i)
'''
# next() nos devuelve el siguiente valor
print(next(sucesionPares))

print("Ahora va el siguiente valor: ")

print(next(sucesionPares))