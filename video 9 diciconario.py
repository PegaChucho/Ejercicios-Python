midiccionario={"Alemania":"Berlin","Francia":"Paris","Mexico":"CDMX"}
midiccionario["Peru"]="Lisboa"
#print(midiccionario)
midiccionario["Peru"]="Lima"
#print(midiccionario)

del midiccionario["Peru"]
#print(midiccionario)


midiccionario2={23:"Jordan","Mosqueteros":3,"Xpetrus":"Clavel"}
print(midiccionario2)

mitupla=["Espagna","Mexico","Francia","Reino Unido"]
midiccionario3={mitupla[0]:"Madrid",mitupla[1]:"CDMX",mitupla[2]:"Paris",mitupla[3]:"Londres"}
print(midiccionario3)
print(midiccionario3["Mexico"])

midiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4)
print(midiccionario4["anillos"])
print(midiccionario4.keys())
print(midiccionario4.values())
print(len(midiccionario4))
