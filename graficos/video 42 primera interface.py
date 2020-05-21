from tkinter import *

raiz=Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(0,0)#ancho, alto
raiz.iconbitmap("foto.ico")
raiz.geometry("300x300")
raiz.config(bg="black")

miFrame=Frame()
miFrame.pack(side="bottom", anchor="e") #fill="both", expand="true"
miFrame.config(width="100", height="100")
miFrame.config(bd=10)#tamaño del relieve del borde del frame
miFrame.config(bg="white", relief="groove")
miFrame.config(cursor="pirate")


raiz.mainloop()
