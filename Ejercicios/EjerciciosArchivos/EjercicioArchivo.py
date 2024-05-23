from io import *

archivo_clientes=open("Ejercicios\EjerciciosArchivos\clientes.txt","r", encoding="utf-8")

lineas=archivo_clientes.readlines()

archivo_clientes.close()

# print(lineas)
clientes=[]

for linea in lineas:

    campos=linea.split(";")

    cliente={"Código":campos[0], "Nombre":campos[1], "Dirección":campos[2], "Población":campos[3], "Teléfono":campos[4], "Responsable":campos[5]}

    clientes.append(cliente)

for c in clientes:

    print("Código Artículo={} Nombre={} Dirección={} Población={} Tfno={} Responsable={}"
          .format(c["Código"], c["Nombre"], c["Dirección"], c["Población"], c["Teléfono"], c["Responsable"]))