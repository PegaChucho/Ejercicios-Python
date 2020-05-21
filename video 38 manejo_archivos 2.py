from io import open


# archivo_texto=open("archivo.txt","r")#(nombre, modo[lectura, escritura, append])

# print(archivo_texto.read())

# archivo_texto.seek(0)#posiciona el puntero en el CARACTER (no linea) 0

# print(archivo_texto.read())


# archivo_texto=open("archivo.txt","r")#(nombre, modo[lectura, escritura, append])

# print(archivo_texto.read(11))


# archivo_texto=open("archivo.txt","r")#(nombre, modo[lectura, escritura, append])

# archivo_texto.seek(len(archivo_texto.read())/2)

# print(archivo_texto.read())


# archivo_texto=open("archivo.txt","r")#(nombre, modo[lectura, escritura, append])

# archivo_texto.seek(len(archivo_texto.readline()))

# print(len(archivo_texto.readline()))
# print(archivo_texto.read())

archivo_texto=open("archivo.txt","r+")#(nombre, modo[lectura, escritura, append])

lista_texto=archivo_texto.readlines()

lista_texto[1]="Esta linea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

print(archivo_texto.read())

archivo_texto.close()