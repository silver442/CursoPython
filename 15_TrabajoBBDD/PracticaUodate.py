import sqlite3

miConexion=sqlite3.connect("15_TrabajoBBDD/GestionPedidos")

miCursor=miConexion.cursor()

# Actualizar
# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=34 WHERE ID=2")

# Borrar
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")


miConexion.commit()

miCursor.close()

miConexion.close()