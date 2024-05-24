from tkinter import *

raiz=Tk()

raiz.title("Primera ventana Pyhton")

# resizable(horizontal,vertical) para redimencionar la ventana
raiz.resizable(1,1)

# cambiar el icono
raiz.iconbitmap("11_InterfacesGraficas\imagen.ico")

# darle una dimension
raiz.geometry("700x400")

# cambiar el color de fondo
raiz.config(bg="green") # bg es de brackground

# bucle infinito para que no se cierre la ventana
raiz.mainloop()