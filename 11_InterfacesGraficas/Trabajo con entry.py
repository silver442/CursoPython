from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()

cuadroTextoNombre=Entry(miFrame)
cuadroTextoNombre.grid(row=0, column=1)
cuadroTextoNombre.config(fg="red")

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1)

cuadroTextoMail=Entry(miFrame)
cuadroTextoMail.grid(row=2, column=1)

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1)


nombreLabelNombre=Label(miFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky="w") # sticky la alineación del texto

nombreLabelApellido=Label(miFrame, text="Apellido: ")
nombreLabelApellido.grid(row=1, column=0, sticky="w")

nombreLabelMail=Label(miFrame, text="Email: ")
nombreLabelMail.grid(row=2, column=0, sticky="w")

nombreLabelDireccion=Label(miFrame, text="Dirección del hogar: ")
nombreLabelDireccion.grid(row=3, column=0, sticky="w")

raiz.mainloop()