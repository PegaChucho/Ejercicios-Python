salario_presidente=int(input("Introduce el salario del presidente: \n"))
print("Salario del presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: \n"))
print("Salario del director: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: \n"))
print("Salario del jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del personal administrativo: \n"))
print("Salario del personal administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona en orden")
else: 
	print("Los salarios no tienen sentido")