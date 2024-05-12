misDatos=["Silver", 13, 1, 2002]

# Converir la lista en una tupla
misDatosTupla=tuple(misDatos)

print(misDatosTupla)

# saber si un elemento se encuentra dentro de una tupla
print(13 in misDatosTupla)

# saber cuantas veces esta el elemento
print(misDatosTupla.count("Silver"))

# para saber la longitud de la tupla
print(len(misDatosTupla))

# Desempaquetado de tupla // guardar cada valor en una variable
misDatos2=("Silver", 13, 1, 2002)
nombre, dia, mes, agno =misDatos2

print(mes)

