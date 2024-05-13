# * para establecer un numero indeterminado de parametros
# y ademas lo toma como una tupla
def capitales_mundo(*ciudades):
    for capital in ciudades:
        #for letra_capital in capital:
            yield from capital # acceder a los sub-elementos
        

capitales_devueltas=capitales_mundo("Berlín","Roma","Bogota","Pekin","Hanoi")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))