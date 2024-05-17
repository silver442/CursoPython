class Persona():
    __nombre=""
    apellido=""
    __edad=0
    genero="sin definir"

    # metodo constructor
    def __init__(self, nombre, apellido, genero):
        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero

    def setEdad(self, laEdad):
        if laEdad<0 or laEdad>100:
            print("Error en la edad")
        else:
            self.__edad=laEdad
            return self.__edad

    def hablar(self):

        return "La persona que se llama " + self.__nombre + " esta hablando"

    def camina(self):

        return "La persona que se llama " + self.__nombre + " esta caminando"

    def getDatos(self):

        return "nombre: " + self.__nombre + " Apellido: " + self.apellido + \
             " edad: " + str(self.__edad) + " Generp: " + self.genero
    
p1=Persona("Silvestre", "Hernandez", "mascullino")

p1.setEdad(-7)

print(p1.getDatos())
