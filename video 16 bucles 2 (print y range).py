#for i in range(5,51,5):
	#print(f"Valor de la variable= {i}")

valido=False
email=input("Introduce tu e-mail: \n")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")
