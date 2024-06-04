import sqlite3

miConexion=sqlite3.connect("15_TrabajoBBDD/miBBDD")

miCursor=miConexion.cursor()

# Creacion de una tabla productos
# miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("SELECT * FROM PRODUCTOS")

# fetchall() convierte los registros de la tabla en una lista
muchosProductos=miCursor.fetchall()

# print(muchosProductos)

for p in muchosProductos:
    print("Nombre: ", p[0], " Precio:", p[1])

# cada vez que se hace una modificacion hay que confirmar con commit()
# Para leer no es necesario el commit
# miConexion.commit()

miCursor.close()

miConexion.close()