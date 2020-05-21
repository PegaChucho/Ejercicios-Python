from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()#con esto le decimos que es una cadena de caracteres

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, pady=10, padx=10)
cuadroNombre.config(fg="red", justify="center")

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", pady=10, padx=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, pady=10, padx=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", pady=10, padx=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2, column=1, pady=10, padx=10)
cuadroPassword.config(show="*")

PasswordLabel=Label(miFrame, text="Contraseña:")
PasswordLabel.grid(row=2, column=0, sticky="e", pady=10, padx=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, pady=10, padx=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", pady=10, padx=10)

cuadroComentarios=Text(miFrame, width=16, height=4)
cuadroComentarios.grid(row=4, column=1, pady=10, padx=10)

scrollVertical=Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew") #con nsew se adapta el scroll al tamaño vertical del texto
cuadroComentarios.config(yscrollcommand=scrollVertical.set)#el vertical.set hace que el scroll se posicione 
#automaticamente en la parte de texto que deseemos'''  

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", pady=10, padx=10)

def codigoBoton():
	minombre.set("Jesús")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()