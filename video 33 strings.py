nombre_usuario=input("Ingrese su nombre: ")
print("El nombre es: ", nombre_usuario.capitalize())

edad=input("Introduzca su edad en años: ")

if edad.isdigit() and int(edad)>0 and int(edad)<99:
	print("Su edad es de ", edad, " años.")
else:
	print("No sea mamón")