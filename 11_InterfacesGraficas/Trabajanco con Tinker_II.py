from tkinter import *

raiz=Tk()

raiz.title("Primera ventana Pyhton")

# resizable(horizontal,vertical) para redimencionar la ventana
raiz.resizable(1,1)

# cambiar el icono
raiz.iconbitmap("11_InterfacesGraficas\imagen.ico")

# darle una dimension
# raiz.geometry("700x400")

# cambiar el color de fondo
raiz.config(bg="green") # bg es de brackground

# Creación de frame
miFrame=Frame()

# Empaquetado del frame
# miFrame.pack(side="right", anchor="n")
# miFrame.pack(fill="x") # fill para rellenar en el eje de las x
miFrame.pack(fill="both", expand=True) # both para expandir en x y y

miFrame.config(bg="red")

# Darle tamaño
miFrame.config(width="650", height="350")

# bucle infinito para que no se cierre la ventana
raiz.mainloop()