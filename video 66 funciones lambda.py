'''def area_triangulo(base, altura):
	return (base*altura)/2

print("El áarea del triangulo 1 es: ", area_triangulo(5,7))


triangulo2= area_triangulo(9,9)
triangulo3= area_triangulo(9,18)

print(triangulo2)
print(triangulo3)'''

area_triangulo=lambda base, altura: (base*altura)/2  #los dos puntos significan return

print(area_triangulo(5,7))

alCubo=lambda numero: pow(numero, 3) #(número, exponente)

print (alCubo(34))

destacar_valor= lambda comision: "¡{}! $".format(comision)

comisionAna=4543322

print(destacar_valor(comisionAna))

