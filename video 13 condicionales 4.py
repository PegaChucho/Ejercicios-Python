print("Programa de becas de Chucho 2019")
distancia_escuela=int(input("Introduce la distancia que recorres de tu casa a la escuela en Km "))
numero_hermanos=int(input("Cuantos hermanos tienes? "))
salario_familiar=int(input("Cual es tu ingreso mensual? "))

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Felicidades! Eres candidato para concursar por una beca")
else: 
	print("Lo sentimos :c , no eres candidato para otorgarle una beca")