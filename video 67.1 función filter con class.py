class Empleado:

	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[

Empleado("Juan", "Director", 75000),
Empleado("Jesús", "CEO", 143000),
Empleado("Héctor", "Jefe de proyecto", 10000),
Empleado("Rafaél", "Becario", 8000),
Empleado("Luz", "Administrador", 110000)

]

print(listaEmpleados)

salariosAltos=filter(lambda empleado: empleado.salario>=100000,listaEmpleados)

for empleado_salario in salariosAltos:
	print (empleado_salario)