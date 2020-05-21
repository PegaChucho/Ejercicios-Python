email=False
j=0
correo=input("Ingresa tu dirección de correo: \n")
for i in correo:
	if(i=="@" or i=="."):
		email=True
	j=j+1

if email==True:
	print("El email es correcto")
else:
	print("El email es incorrecto")

print(j)

for k in range(3):
	print("hola")