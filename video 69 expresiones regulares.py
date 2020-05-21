import re

cadena="Vamos a aprender expresiones regulares en Python. Phyton es un lenj¿guaje de sintaxis sencilla y facil de aprender"

textoBuscar="aprender"

print(re.search("aprender", cadena)) #devuelve el texto si encuentra la plabra

if re.search(textoBuscar,cadena) is not None:
	print ("He encontrado el texto")
else:
	print ("No lo encontré, aiñ :c")


textoEncontrado=re.search(textoBuscar, cadena)	

print (textoEncontrado.start()) #indice en la cadena de donde inicia la palabra que buscamos

print (textoEncontrado.end()) #indice donde termina

print (textoEncontrado.span()) #inicio y fin al mismo tiempo

print (re.findall(textoBuscar, cadena)) #crea una lista con todas las coincidencias

print (len(re.findall(textoBuscar, cadena))) #nos podría decir cuantas coincidencias hay

