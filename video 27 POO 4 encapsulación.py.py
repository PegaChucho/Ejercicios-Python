class coche():
	def __init__(self):

		self.largoChasis=250
		self.anchoChasis=120
		self.__llantas=4 #propiedad encapsulada
		self.enmarcha=False

	def arrancar(self, arrrancamos):
		self.enmarcha=arrrancamos

		if(self.enmarcha)==True:	
			return "El coche está en marcha"
		else:
			return "El coche está parado"

	def estado(self):
		print("El coche tiene ", self.llantas, 
		" ruedas. Un ancho de ", self.anchoChasis, 
		" y un largo de ", self.largoChasis, ".")

miCoche=coche()

print ("El largo del chasis es: " + str(miCoche.largoChasis))
print ("El coche tiene " ,miCoche.llantas, " llantas")
print(miCoche.arrancar(True))

miCoche.estado()#Se pone ... .estado() para acceder al comportamiento.


print("-------Se crea el segundo objeto-----")


miCoche2=coche()

print ("El largo del chasis es: " + str(miCoche2.largoChasis))
print ("El coche tiene " ,miCoche2.llantas, " llantas")
print(miCoche.arrancar(False))

miCoche2.estado() #Se pone ... .estado() para acceder al comportamiento.
