email=False
j=0
k=0
correo=input("Ingresa tu dirección de correo: \n")
for i in correo:
	if(i=="@"):
		j=j+1
	if(i=="."):
		k=k+1

if (j==1) and (k>0 and k<3):
	print("El email es correcto")
else:
	print("El email es incorrecto")



