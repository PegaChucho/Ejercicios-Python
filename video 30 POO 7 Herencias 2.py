class vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ",self.modelo,
			"\nEn marcha: ", self.enmarcha, "\nAcelerando: ",self.acelera,
			"\nFrenando: ", self.frena)


class moto(vehiculos):
	
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ",self.modelo,
			"\nEn marcha: ", self.enmarcha, "\nAcelerando: ",self.acelera,
			"\nFrenando: ", self.frena,"\n", self.hcaballito)

class VElectricos():
	def __init__(self):
		self.autonomia=100

	def cargarEnergia(self):
		self.cargandoE=True

class furgoneta(vehiculos):

	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta esta vacía"

miFurgoneta=furgoneta("Toyota", "Hiace")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miMoto=moto("Honda","XR-290")
miMoto.caballito()
miMoto.estado()

class bElectrica(VElectricos,vehiculos):
	pass

miBici=bElectrica()