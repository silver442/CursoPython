import re

from tkinter import *

from Resultados_Pantalla import *

def pulsaciones_teclas(self, valor, mostrar):

    if mostrar:
        self.operacion+=str(valor)
        mostrar_pantalla(self,valor)
    elif not mostrar and valor=="=":
        self.operacion=re.sub(u"\u00D7","*", self.operacion)
        borrar_pantalla(self)
        mostrar_pantalla(self, str(eval(self.operacion)))
    else:
        pass