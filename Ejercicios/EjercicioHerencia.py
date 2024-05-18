class Vehiculo():

    def __init__(self, color, ruedas, ancho, alto, marchas):
        self.color=color
        self.ruedas=ruedas
        self.ancho=ancho
        self.alto=alto
        self.marcahas=marchas
        self.acelerando=False
        self.frenando=False
        self.girando=False
        
    def acelerar(self):
        self.acelerando=True
    
    def frenar(self):
        self.frenando=True
    
    def girarando(self):
        self.girando=True

class Coche(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto, asientos, marchas, aireCondicionado):
        super().__init__(color, ruedas, ancho, alto, marchas)
        self.asientos=asientos
        self.aireCondicionado=aireCondicionado

    def ir_Marcha_Atras(self):
        self.marcha_Atras=True    

    def arrancar(self):
        self.arrancar=True

class Furgoneta(Coche):

    def __init__(self, color, ruedas, ancho, alto, asientos, aireCondicionado, carga):
        super().__init__(color, ruedas, ancho, alto, asientos, aireCondicionado)
        self.carga=carga
    
    def cargar(self):
        self.cargando=True
    
class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto, marchas):
        super().__init__(color, ruedas, ancho, alto, marchas)

    def saltar(self):
        self.saltando=True

    def derrapar(self):
        self.derrapar=True

class Moto(Coche, Bicicleta):

    def __init__(self, color, ruedas, ancho, alto, cilindrado, asientos):
        super().__init__(color, ruedas, ancho, alto, cilindrado, asientos, aireAcondicionado=False)
        

