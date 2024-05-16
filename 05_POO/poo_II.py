class Persona():
    nombre=""
    apellido=""
    edad=0
    genero="sin definir"

    # metodo constructor
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.genero=genero

    def hablar(self):

        return "La persona que se llama " + self.nombre + " esta hablando"

    def camina(self):

        return "La persona que se llama " + self.nombre + " esta caminando"

    def getDatos(self):

        return "nombre: " + self.nombre + " Apellido: " + self.apellido + \
             " edad: " + str(self.edad) + " Generp: " + self.genero
    
p1=Persona("Silvestre", "Hernandez", 24, "mascullino")

print(p1.getDatos())
