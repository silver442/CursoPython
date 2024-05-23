from io import open

archivo_externo=open("primerArchivo.txt","r") 

# archivo_externo.seek(len(archivo_externo.read())/2)
archivo_externo.seek(len(archivo_externo.readline()))

print(archivo_externo.read())