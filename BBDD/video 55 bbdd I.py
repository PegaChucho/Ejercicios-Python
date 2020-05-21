import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor() #crea el puntero

#MiCursor.execute("CREATE IF NOT EXISTS TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCIÓN VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")

miConexion.commit()#verifica si se quieren hacer esos cambios

miConexion.close()