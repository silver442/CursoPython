from io import open

# archivo_externo=open("primerArchivo.txt","w") # w ecribir
# archivo_externo=open("primerArchivo.txt","a") # a modificar
archivo_externo=open("primerArchivo.txt","r") # r leer

# archivo_externo.write("Bienvenidos a los archivos externos")

# modificar lo que hay
# archivo_externo.write("\nGuardamos información de forma permanente")

# leer información
# informacion=archivo_externo.read()

#leer linea a linea
# readline() devuelve la primer linea
# informacion_lineas=archivo_externo.readline()

# readlines() devuelve las lineas, metiendo cada linea en una lista
informacion_lineas=archivo_externo.readlines()

# print(informacion)
archivo_externo.close()
print(informacion_lineas)
print(informacion_lineas[0])