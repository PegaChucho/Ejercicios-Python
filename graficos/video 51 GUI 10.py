from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montaña=IntVar()
turismoRural=IntVar()

def opcionesViaje():

	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+=" Playa"

	if(montaña.get()==1):
		opcionEscogida+=" Montaña"

	if(turismoRural.get()==1):
		opcionEscogida+=" Turismo Rural"

	textoFinal.config(text=opcionEscogida)

foto = ImageTk.PhotoImage(Image.open('avion.png'))
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()