class Persona():

    def __init__(self, **datos): # **pasar un diccionario

        # items devuelve una lista con clave:valor
        elementos=datos.items()

        for clave, valor in elementos:

            print(clave, " ", valor)
       

p1=Persona(Nombre="silver", Apellido="Hernandez", Edad=18)
