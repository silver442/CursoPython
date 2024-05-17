class Persona():

    def __init__(self, nombre, apellido, edad):
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)
    
    def habla(self):

        return "Estoy hablando"
    
    def pensar(self):

        return "Estoy pensando"
    
    def camina(self):

        return "Estoy caminando"
    
    def come(self):

        return "Estoy comiendo"
    
# Clase que hereda de Persona
class Estudiante(Persona):

    def __init__(self,nombre, apellido, edad, escuela):
        
        super().__init__(nombre,apellido,edad)

        self.escuela=escuela

    # sobre escritura de metodo
    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"
    
persona1=Persona("Anna", "Gómez", 35)

estudiante1=Estudiante("Juan", "Diaz", 21, "San Javier")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())