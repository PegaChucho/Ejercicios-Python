palabra=input("Ingresa una palabra: \n")

j=0
for i in palabra:
	if i==" ":
		continue
	j+=1

print(f"Numero de letras= {j}")
for letra in palabra:
	if letra=="h":
		continue
	print("Viendo la letra " + str(letra))