class Empleado:

	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de ${} incluida su comisión".format(self.nombre, self.cargo, self.salario)




listaEmpleados=[

Empleado("Juan", "Director", 75000),
Empleado("Jesús", "CEO", 143000),
Empleado("Héctor", "Jefe de proyecto", 10000),
Empleado("Rafaél", "Becario", 8000),
Empleado("Luz", "Administrador", 110000)

]

def calculo_comision(empleado):
	if empleado.salario<= 100000:
		empleado.salario *= 1.03
	return empleado #si identas esta sentencia igual que la de arriba, los empleados que ganan mas de 100000 serán mostrados como "none"


listaComisiones=map(calculo_comision, listaEmpleados)

for empleado in listaComisiones:
	print(empleado)