class Persona():
                    # datos es una tupla
    def __init__(self, nom, ape, edad): # *numerso indeterminado de parametros

        self.nombre=nom
        self.apellido=ape
        self.edad=edad

    # El metodo string siempre tiene que devolver un string
    # def __str__(self):   
    #    return "Datos de la persona: \nNombre: " + self.nombre + "\nApellido: "+ self.apellido+ "\nEdad: "+str(self.edad)
    
    # El metodo repr es igual que el método string
    # este método es mucho más preciso
    def __repr__(self):   
       return "Datos de la persona: \nNombre: " + self.nombre + "\nApellido: "+ self.apellido+ "\nEdad: "+str(self.edad)

p1=Persona("Juan","Díaz",18)

print(p1) # imprime la posicion de memoria que ocupa el objeto