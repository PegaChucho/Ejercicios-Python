class coche():
	def __init__(self): #Método constructor

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__llantas=4 #propiedad encapsulada
		self.__enmarcha=False

	
	def __chequeo_interno(self): #con el __ al principio se encapsula el método y solo se puede usar internamente sin llamarlo por fuera (ej: miCoche.chequeo_interno)
		print("Realizando chequeo")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False

	def arrancar(self, arrrancamos):
		self.__enmarcha=arrrancamos #las variables encapsuladas se llaman con__ al inicio

		if(self.__enmarcha)==True:	
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo)==True:	
			return "El coche está en marcha"
		elif(self.__enmarcha==True and chequeo==False):
			return "Algo ha ido mal en el chequeo, el coche no ha arrancado"
		else:
			return "El coche está parado"

	def estado(self):
		print("El coche tiene ", self.__llantas, 
		" ruedas. Un ancho de ", self.__anchoChasis, 
		" y un largo de ", self.__largoChasis, ".")


miCoche=coche()

print(miCoche.arrancar(True))

miCoche.estado()#Se pone ... .estado() para acceder al comportamiento.


print("-------Se crea el segundo objeto-----")


miCoche2=coche()


print(miCoche.arrancar(False))

miCoche2.estado() #Se pone ... .estado() para acceder al comportamiento.
