print("Asignaturas optativas 2019")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion = raw_input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")