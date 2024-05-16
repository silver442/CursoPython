class Coche():
    # propiedades o caracteristicas
    ruedas=4
    largoChasis=260
    anchoChasis=130
    arrancado=False

    # comportamientos
    def arrancar(self): # self se refiere al propio objeto, igual que el this
        self.arrancado=True

    def estadoCoche(self):
        if(self.arrancado):
            return "El coche esta funcionando"

        else:
            return "El coche está parado"

mazda=Coche() # ejemplar de clase

renault=Coche()

print("Tu coche tiene " + str(mazda.ruedas) + " ruedas")

renault.arrancar()

print(renault.estadoCoche())
