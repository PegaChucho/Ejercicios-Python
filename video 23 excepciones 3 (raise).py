def evaluaEdad (edad):

	if edad<0:
		raise TypeError("Nadie puede tener menos de 0 años")
	elif edad<18:
		return "Eres muy joven"
	elif edad<40:
		return "Eres un adulto"
	elif edad<65:
		return "Eres mayor"
	elif edad<100:
		return "Estás muy viejito"

print(evaluaEdad(int(input("Ingresa tu edad: \n"))))