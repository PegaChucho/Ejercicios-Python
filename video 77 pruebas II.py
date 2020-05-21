import math
import doctest

def raizCuadrada(listaNumeros):
	'''
	La función deuelve una lista con la raíz cuadrada
	de los elementos numéricos pasados por 
	parámetros en otra lista

	>>> lista=[]
	>>> for i in [4, 9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]


	>>> lista=[]
	>>> for i in [4, 9, -16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
  		...
	ValueError: math domain error


	'''
	return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([1, 4, 9, -16, 25, 36,49, 81, 100]))

doctest.testmod()