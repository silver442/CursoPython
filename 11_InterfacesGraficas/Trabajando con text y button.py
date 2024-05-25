from tkinter import *

from tkinter import messagebox as MessageBox

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()

miVariable=StringVar()

cuadroTextoNombre=Entry(miFrame, textvariable=miVariable)
cuadroTextoNombre.grid(row=0, column=1, padx=15, pady=15)
cuadroTextoNombre.config(fg="red")

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1, pady=15)

cuadroContra=Entry(miFrame)
cuadroContra.grid(row=2, column=1, pady=15)
cuadroContra.config(show="*") # para que aparesca * en vez de la contraseña

cuadroTextoMail=Entry(miFrame)
cuadroTextoMail.grid(row=3, column=1, pady=15)

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=4, column=1, pady=15)

# Incluir cuadro de texto
cuadroTextoOpiniones=Text(miFrame, width=15, height=10)
cuadroTextoOpiniones.grid(row=5, column=1, padx=15, pady=15)

# Creación de Scrollbar
miScrollVertical=Scrollbar(miFrame, command=cuadroTextoOpiniones.yview)
miScrollVertical.grid(row=5, column=2, sticky="nsew")

cuadroTextoOpiniones.config(yscrollcommand=miScrollVertical.set)

nombreLabelNombre=Label(miFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky="e") # sticky la alineación del texto

nombreLabelApellido=Label(miFrame, text="Apellido: ")
nombreLabelApellido.grid(row=1, column=0, sticky="e")

nombreLabelContra=Label(miFrame, text="Contraseña: ")
nombreLabelContra.grid(row=2, column=0, sticky="e")

nombreLabelMail=Label(miFrame, text="Email: ")
nombreLabelMail.grid(row=3, column=0, sticky="e")

nombreLabelDireccion=Label(miFrame, text="Dirección: ")
nombreLabelDireccion.grid(row=4, column=0, sticky="e")

nombreLabelComentarios=Label(miFrame, text="Comentarios: ")
nombreLabelComentarios.grid(row=5, column=0, sticky="e")

def funcionBoton():

    # MessageBox.showinfo("Saludo", "Hola desde Tkinter")
    miVariable.set("Silver")

# Creacion de boton
botonEnviar=Button(raiz, text="Enviar", command=funcionBoton)
botonEnviar.pack()

raiz.mainloop()