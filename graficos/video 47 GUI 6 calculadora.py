from tkinter import *

raiz=Tk()

miframe=Frame(raiz)

miframe.pack()

operacion=""
resultado=0

#--------pantalla----------------------------
numeroPantalla=StringVar()

pantalla=Entry(miframe, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#--------pulsaciones teclado-----------------

def numeroPulsado(num):
	global operacion
	if operacion != "":
		numeroPantalla.set(num)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get()+num)

def suma(num):
	global operacion
	global resultado
	resultado+=float(num) #resultado=resultado+int(sum)
	operacion ="suma"
	numeroPantalla.set(resultado)

def resta(num):
	global operacion
	global resultado
	resultado=float(resultado)-float(num) #resultado=resultado+int(sum)
	operacion ="resta"
	numeroPantalla.set(resultado)

def multiplicacion(num):
	global operacion
	global resultado
	resultado=float(resultado)*float(num) #resultado=resultado+int(sum)
	operacion ="multiplicacion"
	numeroPantalla.set(resultado)

def division(num):
	global operacion
	global resultado
	resultado=float(resultado)/float(num) #resultado=resultado+int(sum)
	operacion ="division"
	numeroPantalla.set(resultado)

def el_resultado():
	global resultado
	global operacion
	if operacion == "suma":
		numeroPantalla.set(float(resultado)+float(numeroPantalla.get()))
		resultado=0

	elif operacion == "resta":
		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))
		resultado=0

	elif operacion == "multiplicacion":
		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))
		resultado=0

	elif operacion == "division":
		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
		resultado=0

	else:
		numeroPantalla.set(float(numeroPantalla.get()))


def borrar():
	global operacion
	global resultado
	numeroPantalla.set("")
	resultado=0
	operacion=""

#--------fila 789 / -----------------
boton7=Button(miframe, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miframe, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miframe, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botondiv=Button(miframe, text="/", width=3, command=lambda:division(numeroPantalla.get()))
botondiv.grid(row=2, column=4)

#--------fila 456 * -----------------
boton4=Button(miframe, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miframe, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miframe, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonmult=Button(miframe, text="x", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonmult.grid(row=3, column=4)

#--------fila 123 - -----------------
boton1=Button(miframe, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miframe, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miframe, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonrest=Button(miframe, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonrest.grid(row=4, column=4)

#--------fila 0.=+ -----------------
boton0=Button(miframe, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonpunto=Button(miframe, text=".", width=3, command=lambda:numeroPulsado("."))
botonpunto.grid(row=5, column=2)
botonigual=Button(miframe, text="=", width=3, command=lambda:el_resultado())
botonigual.grid(row=5, column=3)
botonsuma=Button(miframe, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonsuma.grid(row=5, column=4)

#--------borrar------------------------
botondel=Button(miframe, text="BORRAR", command=lambda:borrar())
botondel.grid(row=6, column=1, columnspan=4)

raiz.mainloop()