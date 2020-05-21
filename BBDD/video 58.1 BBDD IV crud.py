import sqlite3

miConexion=sqlite3.connect("GestiónProductos")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION ='CONFECCIÓN'")

productos_leidos= miCursor.fetchall()
columnas= miCursor.description

print (productos_leidos)
print(columnas)

for i in productos_leidos:
	for j in i:
		print(j)

	
miConexion.commit()

miConexion.close()