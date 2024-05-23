import os

import io

# creación de directorio
os.makedirs("PracticaDirectorio")

# moverse al directorio creado
os.chdir("PracticaDirectorio")

archivo_externo=open("Ejemplo.txt", "w")

archivo_externo.write("Texto de ejemplo...")

# imprime la ruda del directorio
print(os.getcwd())

# en lista todo el contenido que tiene ese directorio
print(os.listdir("./"))