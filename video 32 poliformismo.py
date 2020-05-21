class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")

mivehiculo=Moto()
mivehiculo.desplazamiento()

mivehiculo2=Coche()
mivehiculo2.desplazamiento()

mivehiculo3=Camion()
mivehiculo3.desplazamiento()

#-------------------------------------------------
def desplazamiento_vehiculo(vehiculo):
	vehiculo.desplazamiento()

mivehiculo4=Camion()
desplazamiento_vehiculo(mivehiculo4)