class coche():
	largoChasis=250
	anchoChasis=120
	llantas=4
	enmarcha=False

	def arrancar(self):	
		self.enmarcha=True

	def estado(self):
		if (self.enmarcha)==True:
			return "El coche está en marcha"
		else:
			return "El coche está parado"

miCoche=coche()

print ("El largo del chasis es: " + str(miCoche.largoChasis))
print ("El coche tiene " ,miCoche.llantas, " llantas")
miCoche.arrancar()

print (miCoche.estado()) #Se pone ... .estado() para acceder al comportamiento.