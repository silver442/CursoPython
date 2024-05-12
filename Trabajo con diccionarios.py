
lasCapitales={"España":"Madrid","Francia":"Toulousse","Reino Unido":"Londres"}

# Agregar un nuevo valor [Clave] = valor
lasCapitales["Colombia"]="Bogota"

# Cambiar un valor
lasCapitales["Francia"]="Paris"

print(lasCapitales)

# Eliminar un valor
del lasCapitales["Reino Unido"]

print(lasCapitales)

# Creación de tupla para usarla como clave para el diccionario

claveCapitales=["España", "Reino Unido", "Colombia", "Portugal"]

capitalaesMundo={claveCapitales[0]:"Madrid",claveCapitales[1]:"Londres", claveCapitales[2]:"Bogotá", claveCapitales[3]:"Lisboa"}

print(capitalaesMundo)

# acceder a un elemento
print(capitalaesMundo["Colombia"])

# saber cual son las claves
print(capitalaesMundo.keys())

# Imprimir todos los valores
print(capitalaesMundo.values())

# conocer la longitud
print(len(capitalaesMundo))

# Creacion de diccionario con diferentes tipos
datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"c Bulls","anillos":[1991,1992,1993,1996,1997,1998]}

# accediendo a los campeonatos
print(datosJordan["anillos"])

# Diccionario dentro de otro
datosJordan2={23:"Jordan", "Nombre":"Michael", "Equipo":"c Bulls","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(datosJordan2.keys())