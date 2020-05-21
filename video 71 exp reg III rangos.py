import re

lista_nombres=[
				"Ana",
				"Pedro",
				"María",
				"Rosa",
				"Celia",
				"Sandra",
				"Ma1",
				"Ma2",
				"Ma3",
				"Se1",
				"Se2",
				"Ma4",
				"Se3",
				"SeA",
				"SeB",
				"SeC",
				"Bu.1",
				"Cuau:3"
				]

for elemento in lista_nombres:
	if re.findall('[o-t]', elemento): #Muestra los nombres que contengan letras en un rango de la o a la t
		print (elemento)

print()

for elemento in lista_nombres:
	if re.findall('[o-t]$', elemento): #Muestra los nombres que terminen con letras en un rango de la o a la t
		print (elemento)

print()

for elemento in lista_nombres:
	if re.findall('^[O-T]', elemento): #Muestra los nombres que empiecen con letras en un rango de la o a la t
		print (elemento)
print()

for elemento in lista_nombres:
	if re.findall('Ma[1-3]', elemento): #Muestra los nombres que empiecen con letras Ma y cualquier numero entre 1 y 3
		print (elemento)

print()

for elemento in lista_nombres:
	if re.findall('Ma[^1-3]', elemento): #Muestra los nombres que empiecen con letras Ma y cualquier otro fuera de 1 y 3
		print (elemento)

print()

for elemento in lista_nombres:
	if re.findall('Se[1-3A-C]', elemento): #Muestra los nombres que empiecen con letras Ma y cualquier otro fuera de 1 y 3
		print (elemento)

print()

for elemento in lista_nombres:
	if re.findall('[.:]', elemento): #Muestra los nombres que empiecen con letras Ma y cualquier otro fuera de 1 y 3
		print (elemento)