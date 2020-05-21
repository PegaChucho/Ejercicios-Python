def divide():
	while True:
		try:
			op1=(float(input("Introduce el primer número: ")))
			op2=(float(input("Introduce el segundo número: ")))
			print(f"El resultado es: {op1/op2} ")
			break;
		except ValueError:
			print("El valor introducido no es un número")
		except ZeroDivisionError:
			print("No se puede dividir entre 0")

		finally:
			print("Cálculo finalizado")

divide()