
def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs): #con *args puede recibir un numero indeterminado de parámetros, **kwargs sirve para agregar n argumentos del tipo clave-valor
		#acciones adicionales que agregan funcionalidades
		print("Vamos a realizar un cálculo: ")
		funcion_parametro(*args, **kwargs)
		#mas acciones que decoran
		print("Se ha concluido el cálculo.")
	return funcion_interior


@funcion_decoradora #poniendo esto arriba de la funcion se decora con la función decoradora
def suma(num1, num2):
	print(num1+num2)

@funcion_decoradora
def resta(num1,num2):
	print(num1-num2)

@funcion_decoradora
def potencia(base, exp):
	print(pow(base, exp))



suma(7,5)

print() 

resta(17,10)

print()

#potencia(5,3)
potencia(base=5, exp=3)#lo mismo de arriba pero expresado en formato clave-valor, para eso sirve **kwargs