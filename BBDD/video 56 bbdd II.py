import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor() #crea el puntero

#miCursor.execute("CREATE IF NOT EXISTS TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCIÓN VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")

# variosProductos=[
	
# 	("Camiseta", 10, "Deportes"),
# 	("Jarrón", 90, "Cerámica"),
# 	("Camión", 10, "Juguetería"),

# 	]

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall() #devuelve una lista que devuelve el select de SQL

for producto in variosProductos:
	print("Nombre del artículo: ", producto[0], ", Sección: ", producto[2],"." )
	

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos )

miConexion.commit()#verifica si se quieren hacer esos cambios

miConexion.close()