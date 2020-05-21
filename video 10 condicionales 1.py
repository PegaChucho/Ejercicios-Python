print("Programa de evaluacion de calificaciones de alumnos")
calif_alumno=input("Introduce la calificacion del alumno: ")

def evaluacion (calif): 
	valoracion="aprobado"
	if calif < 6: 
		valoracion="reprobado"
	return valoracion

print (evaluacion(int(calif_alumno)))