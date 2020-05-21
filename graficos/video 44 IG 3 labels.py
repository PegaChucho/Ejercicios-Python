from tkinter import *

root=Tk()

miFrame=Frame(root, width="500", height="500")
miFrame.pack()

miImagen=PhotoImage(file="descarga.png")
#miLabel=Label(miFrame, text="Brenda, estás hermosa")
#miLabel.place(x="250", y="250")
Label(miFrame,image=miImagen).place(x=0,y=0)
Label(miFrame, text="Brenda, estás hermosa", fg="red", font=("Comic Sans MS", "20")).place(x=200, y=200)


root.mainloop()