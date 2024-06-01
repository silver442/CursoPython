import re

lista_terminos=["camión", "camion", "niños", "niñas", "ejemplo"]

# [] para hacer busqueda tanto sin importar el genero
for termino in lista_terminos:
    if re.findall("niñ[oa]s",termino):
        print(termino)
