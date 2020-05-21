import math
print("Prgrama de cálculo de raíz cuadrada")
numero=int(input("Introduce un número: \n"))

i=0

while numero<0:
	print("No se puede hallar la raíz de un número negativo")
	if i==2:
		print("Has hecho demasiados intentos, programa finalizado")
		break;

	numero=int(input("Introduce un número mayor que 0: \n"))
	if numero<0:
		i=i+1

if i <2:
	solucion=  math.sqrt(numero)
	print(f"La raíz de {numero} es = {solucion}")