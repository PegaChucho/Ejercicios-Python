from modulos import funciones_matematicas

class Areas:
	"""Esta clase calcula las áreas de diferentes 
	figuras geométricas"""

	def areaCuadrado(lado):
		'''Calcula el area de un cuadrado
		elevando al cuadrado el lado  pasado por parámetro'''
		return "El área del cuadrado es: " + str(pow(lado,2))

	def areaTriangulo(base, altura):
		'''Calcula el área de un triángulo usando los 
		parámetros base y altura'''
		return "El área del triangulo es: " +str(base*altura/2)

print(Areas.areaCuadrado(8))
print(Areas.areaCuadrado.__doc__)
help(Areas.areaCuadrado)

print()

print(Areas.areaTriangulo(2,7))
help (Areas)

print()

help(funciones_matematicas)