#basado en los videos 45,46, 47
from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------------Funcion decoradora---------------
def decorador(funcionBBDD):
	def funcion_interna(*args, **kwargs):
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()
		funcionBBDD(miConexion, miCursor)
		miConexion.commit()
		miConexion.close()
	return funcion_interna


#-------------------Funciones BBDD---------------

@decorador
def crearBBDD(miConexion, miCursor):
	
	try:
		miCursor.execute(''' 
			CREATE TABLE USUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(25),
			APELLIDOS VARCHAR(25),
			PASSWORD VARCHAR(8),
			DIRECCIÓN VARCHAR(50),
			COMENTARIOS VARCHAR(150))
			''')# LAS COMILLAS SIMPLES PERMITEN CREAR LA MISMA SENTENCIA EN VARIOS RENGLONES

		messagebox.showinfo("BBDD", "La base de datos 'Usuarios' fue creada con éxito")

	except:
		messagebox.showwarning("AVISO:", "La base de datos 'Usuarios' ya existe.")

def salir():
	confirmacion=messagebox.askquestion("¿Deseas salir de la aplicación?")

	if confirmacion == "yes":
		raiz.destroy() #.destroy() cierra la aplicación
		
def borrarPantalla():
	idPantalla.set("")# El set funciona cuando usamos variables del tipo StringVar
	#cuadroID.delete(1.0, END)
	nombrePantalla.set("")
	ApellidosPantalla.set("")
	PasswordPantalla.set("")
	DirecciónPantalla.set("")
	cuadroComentarios.delete(1.0, END)#El .delete no funciona con los StringVar, se borra el objeto "cuadroComentarios" directamente

@decorador
def insertarNuevosBBDD(miConexion, miCursor): 

	nuevosDatos=[ #ejemplo de una consulta parametrizada
	(
	nombrePantalla.get(),
	ApellidosPantalla.get(),
	PasswordPantalla.get(),
	DirecciónPantalla.get(),
	cuadroComentarios.get(1.0, END)# como cuadroComentarios no es StringVar, el .get require de dos argumentos: inicio (1.0 o primer valor) y fin (END)
	)
	]

	miCursor.executemany("INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?)", nuevosDatos) #Inyección SQL

	messagebox.showinfo("BBDD", "Registros añadidos con éxito")

	borrarPantalla()

@decorador
def  leerBBDD(miConexion, miCursor):

	miCursor.execute("SELECT * FROM USUARIOS WHERE ID =" + str(idPantalla.get()))# primera forma de usar el idread

	usuarios= miCursor.fetchall()

	for i in usuarios: #Usuarios es una tupla, cuyo unico (o varios) argumento(s) es una lista adentro que corresponde a los valores de  row (fila o filas)
	#En este caso "i" tomará el valor de la unica lista dentro de la tupla y ya se puede iterar dentro de i: ( i[n])
		nombrePantalla.set(i[1])
		ApellidosPantalla.set(i[2])
		PasswordPantalla.set(i[3])
		DirecciónPantalla.set(i[4])
		cuadroComentarios.insert(1.0, i[5])# (CARACTER DE INICIO, DATOS A AGREGAR) 

@decorador
def actualizarRegBBDD(miConexion, miCursor):

	nuevosDatos=[ 
		(
		nombrePantalla.get(),
		ApellidosPantalla.get(),
		PasswordPantalla.get(),
		DirecciónPantalla.get(),
		cuadroComentarios.get(1.0, END)
		)
		]

	miCursor.executemany("UPDATE USUARIOS SET NOMBRE= ?, APELLIDOS= ?, PASSWORD= ?, DIRECCIÓN= ?,COMENTARIOS= ?" +
	"WHERE ID=" + str(idPantalla.get()), nuevosDatos)
	'''miCursor.execute("UPDATE USUARIOS SET NOMBRE='" + nombrePantalla.get()+ #otra forma
		"', APELLIDOS='" + ApellidosPantalla.get()+
		"', PASSWORD='" + PasswordPantalla.get()+
		"', DIRECCIÓN='" + DirecciónPantalla.get()+
		"', COMENTARIOS='" + cuadroComentarios.get(1.0, END)+
		"' WHERE ID=" + str(idPantalla.get()))''' #segunda forma, sin agregar una variable
		###Se pone el str() para poder concatenar el valor de idPantalla, puesto que originalmente esta declarado como entero intVar()

	messagebox.showinfo("BBDD", "Datos actualizados con éxito")

@decorador
def borrarBBDD(miConexion, miCursor):

	confirmacion=messagebox.askquestion("¿Deseas eliminar el registro de la ID " + str(idPantalla.get()) + " ?")

	if confirmacion == "yes":

		miCursor.execute("DELETE FROM USUARIOS WHERE ID=" + str(idPantalla.get()))

		messagebox.showinfo("BBDD", "El registro de la ID " + str(idPantalla.get()) + " ha sido borrado")

		borrarPantalla()

@decorador
def borrarTodoBBDD(miConexion, miCursor):

	confirmacion=messagebox.askquestion("¿Deseas eliminar todos los registros?")

	if confirmacion == "yes":

		miCursor.execute("DELETE FROM USUARIOS")

		messagebox.showinfo("BBDD", "Todos los registros de la  base de datos 'Usuarios' se eliminaron")



#------barra menu-------------

raiz=Tk()

miFrame=Frame(raiz, width=300, height=300)
miFrame.pack()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=200, height=300)

archivoConectar=Menu(barraMenu, tearoff=0) #con tearoff desaparece el separador ----
archivoConectar.add_command(label="Conectar", command=crearBBDD)
archivoConectar.add_command(label="Salir", command=salir)

archivoBorrar=Menu(barraMenu, tearoff=0)
archivoBorrar.add_command(label="Borrar campos", command=borrarPantalla)

archivoCRUD=Menu(barraMenu, tearoff=0)
archivoCRUD.add_command(label="Crear", command=insertarNuevosBBDD)#Ojo!! llamar a la función sin parentesis para que no arranque sola
archivoCRUD.add_command(label="Leer", command= leerBBDD)
archivoCRUD.add_command(label="Actualizar", command= actualizarRegBBDD)
archivoCRUD.add_command(label="Borrar", command= borrarBBDD)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD", menu=archivoConectar)
barraMenu.add_cascade(label="Borrar", menu=archivoBorrar)
barraMenu.add_cascade(label="CRUD", menu=archivoCRUD)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#------cuerpo de la app-------------

idPantalla=IntVar(value="")
nombrePantalla= StringVar()
ApellidosPantalla=StringVar()
PasswordPantalla=StringVar()
DirecciónPantalla=StringVar()


IDLabel=Label(miFrame, text="ID:")
IDLabel.grid(row=0, column=0, sticky="wens", pady=10, padx=10)
cuadroID=Entry(miFrame, textvariable=idPantalla)
cuadroID.grid(row=0, column=1, pady=10, padx=10)
cuadroID.config(fg="black", justify="center")

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="wens", pady=10, padx=10)
cuadroNombre=Entry(miFrame, textvariable=nombrePantalla)
cuadroNombre.grid(row=1, column=1, pady=10, padx=10)
cuadroNombre.config(fg="black", justify="center")

apellidoLabel=Label(miFrame, text="Apellidos:")
apellidoLabel.grid(row=2, column=0, sticky="wens", pady=10, padx=10)
cuadroapellido=Entry(miFrame, textvariable=ApellidosPantalla)
cuadroapellido.grid(row=2, column=1, pady=10, padx=10)
cuadroapellido.config(fg="black", justify="center")

passwordLabel=Label(miFrame, text="Password:")
passwordLabel.grid(row=3, column=0, sticky="wens", pady=10, padx=10)
cuadropassword=Entry(miFrame, textvariable=PasswordPantalla)
cuadropassword.grid(row=3, column=1, pady=10, padx=10)
cuadropassword.config(fg="black", justify="center", show="*")

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="wens", pady=10, padx=10)
cuadrodireccion=Entry(miFrame, textvariable=DirecciónPantalla)
cuadrodireccion.grid(row=4, column=1, pady=10, padx=10)
cuadrodireccion.config(fg="black", justify="center")

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="wens", pady=10, padx=10)
cuadroComentarios=Text(miFrame, width=16, height=4)
cuadroComentarios.grid(row=5, column=1, pady=10, padx=10)
scrollVertical=Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVertical.grid(row=5, column=2, sticky="nsew") 
cuadroComentarios.config(yscrollcommand=scrollVertical.set)

#--------------botones parte inferior------------------

miFrame2=Frame(raiz) #Se crea otro frame especial para los botones y asi se ajusten independietemente a lo de arriba
miFrame2.pack()

botonCreate=Button(miFrame2, text="Add row", command=insertarNuevosBBDD)
botonCreate.grid(row=0, column=0, pady=5, padx=5)

botonRead=Button(miFrame2, text="Read row", command=leerBBDD)#), command=codigoBoton)
botonRead.grid(row=0, column=1, pady=5, padx=5)

botonUpdate=Button(miFrame2, text="Update row", command=actualizarRegBBDD)
botonUpdate.grid(row=0, column=2, pady=5, padx=5)

botonDelete=Button(miFrame2, text="Delete row", command=borrarBBDD)
botonDelete.grid(row=0, column=3, pady=5, padx=5)

botonDeleteAll=Button(miFrame2, text="Delete all", command=borrarTodoBBDD)
botonDeleteAll.grid(row=0, column=4, pady=5, padx=5)


raiz.mainloop()