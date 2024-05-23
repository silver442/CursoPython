from io import open

archivo_externo=open("primerArchivo.txt","r+") # r+ modo lectura y escritura

lista_archivo=archivo_externo.readlines()

lista_archivo[1]="Hoy es viernes y ya llega el ansiado fin de semana \n"

archivo_externo.seek(0) 

archivo_externo.writelines(lista_archivo)

archivo_externo.close()