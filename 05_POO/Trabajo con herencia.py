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
        
        Persona.__init__(self,nombre,apellido,edad)

        self.escuela=escuela

    # sobre escritura de metodo
    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"

class Trabajador(Persona):
    def __init__(self,nombre, apellido, edad, empresa):
    
        Persona.__init__(self,nombre,apellido,edad)

        self.empresa=empresa

    # sobre escritura de metodo
    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Empresa: " + self.empresa

    def trabaja(self):

        return "Estoy trabajando"

# clase con herencia multiple, las clases heredadas se separan con comas
class Director(Trabajador, Estudiante): # Trabajador tiene preferencia

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):

        Trabajador.__init__(self,nombre, apellido, edad, empresa)
        Estudiante.__init__(self,nombre, apellido, edad, escuela)

        self.bonus=bonus
    
    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Bonus: " + str(self.bonus)
    
    def dirige(self):

        return "Estoy dirigiendo"


persona1=Persona("Anna", "Gómez", 35)

estudiante1=Estudiante("Juan", "Diaz", 21, "San Javier")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
print("------------------------------------------------")

trabajador1=Trabajador("Antonio", "López",55, "c cope")
print(trabajador1.getDatosPersonales())

director1=Director("Juan M", "Díaz", 21, "Pildoras Informaticas", "San javier", 1500)

print(director1.getDatosPersonales())
