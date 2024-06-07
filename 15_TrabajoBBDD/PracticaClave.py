import sqlite3

miConexion=sqlite3.connect("15_TrabajoBBDD/GestionPedidos")

miCursor=miConexion.cursor()

miCursor.execute('''
   CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(40), UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
   )                           
''')

misProductos=[
    ("pelota", 15, "deportes"),
    ("cenicero", 25, "ceramica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?)", misProductos)

miConexion.commit()

miCursor.close()

miConexion.close()