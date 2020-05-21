from io import open

# archivo_texto=open("archivo.txt","w")#(nombre, modo[lectura, escritura, append])

# frase="Estupendo dia para estudiar Python \nel jueves"

# archivo_texto.write(frase) #Manipulación

# archivo_texto.close()


# archivo_texto=open("archivo.txt","r")#(nombre, modo[lectura, escritura, append])

# texto=archivo_texto.read()

# archivo_texto.close()

# print(texto)


# archivo_texto=open("archivo.txt","r")#(nombre, modo[lectura, escritura, append])

# lineas_texto=archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto[0,1])


archivo_texto=open("archivo.txt","a")#(nombre, modo[lectura, escritura, append])

archivo_texto.write("\nSiempre es un buen dia para estudiar Python")