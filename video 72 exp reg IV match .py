import re

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="Jara López"
nombre5="Lara López"

cadena1="Sandra López"
cadena2="2534546547658"
cadena3="d3454657567"

if re.match("Sandra", nombre1): #busca coincidencias al INICIO de una cadena de texto
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print()

if re.match("sandra", nombre1, re.IGNORECASE): #re.IGNORECASE es el flag y desactiva reconocimiento entre máyusculas y minúsculas
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print()

if re.match(".ara", nombre5, re.IGNORECASE): #con .ara ignora el primer caracter
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print()

if re.match("\d", cadena3): #con \d preguntamos si el primer caracter es un número
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print()

if re.search("López", nombre1): #search busca coincidencias en toda la cadena y no solo al principio
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")