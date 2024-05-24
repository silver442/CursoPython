from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=450)

miFrame.pack()

# miLabel=Label(miFrame, text="Hoy son los Santos inocentes")

# ubicar el label o texto
# miLabel.place(x=120, y=125)

# Label(miFrame, text="Hoy son los Santos Inocentes", fg="blue", font=("Courier",20)).place(x=120, y=125)

# tkinter en imagenes trabaja con png y gif
miLogo=PhotoImage(file="facebook.png")

Label(miFrame, image=miLogo).place(x=120, y=125)

root.mainloop()