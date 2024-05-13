nombresPersonas = []

def agregar_a_lista(lista, nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)
    except ValueError:
        print("Error. Este nombre ya se ha introducido: ", nombreIntroducido)

introducidos=1

while introducidos<11:

    nombre=input("Introduce nombre: ")
    agregar_a_lista(nombresPersonas, nombre)
    introducidos+=1

print(nombresPersonas)