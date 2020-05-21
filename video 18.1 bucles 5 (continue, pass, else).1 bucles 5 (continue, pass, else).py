email=input("Introduce tu e-mail: \n")

for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False
print(arroba)