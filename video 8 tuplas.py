mitupla=("Jesus",4,12,1995)
listatupla=list(mitupla)
print(listatupla)

listatupla2=["Jesus",4,12,1995]
mitupla2=tuple(listatupla2)
print(mitupla2)

print("Jesus"in mitupla2)
print(mitupla2.count(1995))
print(len(mitupla2))

nombre,dia,mes,agno= mitupla
print(nombre)