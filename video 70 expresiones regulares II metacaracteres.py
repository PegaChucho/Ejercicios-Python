import re

lista_nombres=[
"http://pildorasinformaticas.es",
"ftp://pildorasinformaticas.es",
"http://pildorasinformaticas.com",
"ftp://pildorasinformaticas.com",
"http://informaticaenespaña.es",
"Ana Gómez",
"Eva García",
"Valentín Pérez",
"Luz Pérez",
"Brenda Altamirano",
"Jesús Pérez",
"Juan Diaz",
"niños",
"niñas",
"termino",
"terminó"
]

for elemento in lista_nombres:
	if re.findall("^Luz", elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)

print("------------------------------")

for elemento in lista_nombres:
	if re.findall("Pérez$", elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)

print("------------------------------")

for elemento in lista_nombres:
	if re.findall("es$", elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)

print("------------------------------")

for elemento in lista_nombres:
	if re.findall("^ht", elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)

print("------------------------------")

for elemento in lista_nombres:
	if re.findall('[ñ]', elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)

print("------------------------------")


for elemento in lista_nombres:
	if re.findall('niñ[oa]s', elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)

print("------------------------------")

for elemento in lista_nombres:
	if re.findall('termin[oó]', elemento): #("^Luz") busca solo los elementos de la lista que empiecen por "Luz"
		print (elemento)