import mysql.connector

miConexion=mysql.connector.connect(host="localhost", database="pruebas", user="root", password="")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM clientes")

muchosAlumnos=miCursor.fetchall()

print(muchosAlumnos)

# miConexion.commit()

miCursor.close()

miConexion.close()