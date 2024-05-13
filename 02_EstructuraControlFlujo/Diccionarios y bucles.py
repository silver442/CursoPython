
capitales={"China":"Pekin","India":"Nueva Delhi","Indonesia":"Yakarta","Japon":"Tokio","Banglades":"Dacca"}

# Acceder a las claves
for clave in  capitales:
    print(clave)

# Recorrer la clave y el valor
for clave in capitales:
    valor=capitales[clave]
    print(clave)
    print(valor)

print(capitales.items())

# otra forma de recorrer el diccionario
for clave, valor in capitales.items():
    print(clave + "->" + valor)
    