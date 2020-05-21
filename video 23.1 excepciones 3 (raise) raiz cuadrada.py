import math
def raiz (num1):

	if num1<0:
		raise ValueError("No existe raíz de un número negativo")
	else:
		return math.sqrt(num1)
	
op1=int(input("Introduce un número: "))

try:
	print(raiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("Programa terminado")