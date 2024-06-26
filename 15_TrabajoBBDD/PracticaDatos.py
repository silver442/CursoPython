import sqlite3

miConexion=sqlite3.connect("15_TrabajoBBDD/miBBDD")

miCursor=miConexion.cursor()

# Creacion de una tabla productos
# miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('Camiseta', 25, 'Moda')")

muchosProductos=[
    ("Patín",100, "Deportes"),
    ("Cenicero", 20, "Cerámica"),
    ("Pantalón", 80, "Moda")

]

# Insertar muchos productos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", muchosProductos)

# cada vez que se hace una modificacion hay que confirmar con commit()
miConexion.commit()

miCursor.close()

miConexion.close()