from tkinter import *

def mostrar_pantalla(self, valor):
    self.display.insert(END, valor)
    
def borrar_pantalla(self):
    self.display.delete(0,END)
