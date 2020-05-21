class Persona():

	def __init__(self, nombre, edad, residencia):

		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia

	def descripcion(self):
		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.residencia)


class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
		self.salario=salario
		self.antigüedad=antigüedad

	def descripcion(self):

		super().descripcion()
		print("Salario: ",self.salario, " Antigüedad: ",self. antigüedad)

Jesus=Empleado(1500, 15, "Jesús", 24, "México")
Brenda=Persona("Brenda", 24, "Buenavista")
Jesus.descripcion()


print(isinstance(Jesus, Empleado))
print(isinstance(Brenda, Empleado))