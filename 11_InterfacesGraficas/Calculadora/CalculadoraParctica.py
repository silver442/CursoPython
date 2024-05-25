from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

display=Entry(miFrame)

display.grid(row=1, column=1, columnspan=4, pady=10)
display.config(background="black", fg="green", justify="right", width=20, font=12)

# ------------------Primera fila----------------------------

boton7=Button(miFrame, text="7", width=4)
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=4)
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=4)
boton9.grid(row=2, column=3)

botondiv=Button(miFrame, text="/", width=4)
botondiv.grid(row=2, column=4)

# ------------------segunda fila----------------------------

boton4=Button(miFrame, text="4", width=4)
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=4)
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=4)
boton6.grid(row=3, column=3)

botonmult=Button(miFrame, text="x", width=4)
botonmult.grid(row=3, column=4)

# ------------------Tercera fila----------------------------

boton1=Button(miFrame, text="1", width=4)
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=4)
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=4)
boton3.grid(row=4, column=3)

botonrest=Button(miFrame, text="-", width=4)
botonrest.grid(row=4, column=4)

# ------------------Cuarta fila----------------------------

boton0=Button(miFrame, text="0", width=4)
boton0.grid(row=5, column=1)

botonpunto=Button(miFrame, text=".", width=4)
botonpunto.grid(row=5, column=2)

botonigual=Button(miFrame, text="=", width=4)
botonigual.grid(row=5, column=3)

botonmas=Button(miFrame, text="+", width=4)
botonmas.grid(row=5, column=4)









raiz.mainloop()