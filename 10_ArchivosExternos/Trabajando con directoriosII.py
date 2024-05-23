import os

import io

listaArchivos=os.listdir("./")

for archivo in listaArchivos:

    if archivo=="tirar.py":

        os.remove(archivo)