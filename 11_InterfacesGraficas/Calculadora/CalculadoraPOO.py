import re
from tkinter import *

raiz=Tk()

class Calculadora:
    def __init__(self, ventana):

        self.ventana=ventana
        self.ventana.title("Calculadora POO")
        self.operacion=""

        # Agregar display

        self.display=Entry(ventana, font="Arial 15")

        # Ubicar display

        self.display.grid(row=1, column=0, columnspan=4, pady=10)
        self.display.config(background="black", fg="#00db00", justify="right", width=25)

        # Creación de botones

        boton7=self.colocar_Boton(7)
        boton8=self.colocar_Boton(8)
        boton9=self.colocar_Boton(9)
        botondiv=self.colocar_Boton("/")

        #------------------------------------------------

        boton4=self.colocar_Boton(4)
        boton5=self.colocar_Boton(5)
        boton6=self.colocar_Boton(6)
        botonx=self.colocar_Boton(u"\u00D7")
        # botonx.config(text="x")

        #------------------------------------------------

        boton1=self.colocar_Boton(1)
        boton2=self.colocar_Boton(2)
        boton3=self.colocar_Boton(3)
        botonrest=self.colocar_Boton("-")

        #------------------------------------------------

        botoncero=self.colocar_Boton(0)
        botoncoma=self.colocar_Boton(".")
        botonigual=self.colocar_Boton("=", mostrar=False)
        botonmas=self.colocar_Boton("+")

        #------------------------------------------------

        botones=[boton7, boton8, boton9, botondiv, boton4, boton5, boton6,
        botonx, boton1, boton2, boton3, botonrest, botoncero, botoncoma, botonigual, botonmas]

        contador=0

        for fila in range(2, 6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1

    def colocar_Boton(self, valor, mostrar=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9),
        command=lambda:self.pulsaciones_teclas(valor, mostrar))

    def pulsaciones_teclas(self, valor, mostrar):

        if mostrar:
            self.operacion+=str(valor)
            self.mostrar_pantalla(valor)
        elif not mostrar and valor=="=":
            self.operacion=re.sub(u"\u00D7","*", self.operacion)
            self.borrar_pantalla()
            self.mostrar_pantalla(str(eval(self.operacion)))
        else:
            pass

    def mostrar_pantalla(self, valor):
        self.display.insert(END, valor)
        
    def borrar_pantalla(self):
        self.display.delete(0,END)

mi_calculadora=Calculadora(raiz)

raiz.mainloop()