# num1=int(input("Introduce el primer numero "))
# num2=int(input("Introduce el segundo numero "))
# num3=int(input("Introduce el tercer numero "))

# prom= (num1+num2+num3)/3

# print(str("El promedio es: "), float(prom))
#----------------------------------------------------------

# num1=input("Introduce el primer numero ")
# num2=input("Introduce el segundo numero ")

# def DevuelveMax(n1, n2):
# 	if n1<n2:
# 		print("El numero 2 es mayor")
# 	elif n1>n2:
# 		print("El numero 1 es mayor")
# 	else:
# 		print("Los numeros son iguales")

# DevuelveMax(num1,num2)
#----------------------------------------------------------

nom=input("Introduce tu nombre: ")
direc=input("Introduce tu direccion: ")
tel=int(input("Introduce tu telefono: "))

lista=[nom,direc,tel]

print("Los datos personales son: "+lista[0]+" "+lista[1]+" "+lista[2])