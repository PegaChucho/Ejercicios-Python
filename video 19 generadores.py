# def generaPares(limite):
# 	num=1
# 	milista=[]
# 	while num<(limite/2):
# 		milista.append(num*2)
# 		num+=1
# 	return milista

# print (generaPares(100))

def generaPares1(limite):
	num=1

	while num<(limite/2):
		yield num*2
		num+=1

devuelvepares=generaPares1(50)

#for i in devuelvepares:
	#print (i)
print(next(devuelvepares))
print("Aquí podría ir mas código...")

print(next(devuelvepares))
print("Aquí podría ir mas código...")