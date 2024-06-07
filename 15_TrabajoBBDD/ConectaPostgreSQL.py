import psycopg2

miConexion=psycopg2.connect(host="localhost", database="Personas", user="postgres", password="pos1234")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM ALUMNOS")

muchosAlumnos=miCursor.fetchall()

print(muchosAlumnos)

# miConexion.commit()

miCursor.close()

miConexion.close()