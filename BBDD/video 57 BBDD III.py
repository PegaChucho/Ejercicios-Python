import sqlite3

miConexion=sqlite3.connect("GestiónProductos")

miCursor=miConexion.cursor()

miCursor.execute(''' 
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
	''')# LAS COMILLAS SIMPLES PERMITEN CREAR LA MISMA SENTENCIA EN VARIOS RENGLONES

productos_insertar=[

	("PELOTA", 20, "JUGUETERIA"),
	("PANTALÓN", 15, "CONFECCIÓN"),
	("DESTORNILLADOR", 25, "FERRETERÍA"),
	("JARRÓN", 45, "CERÁMICA"),

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos_insertar)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('ARO5', 'TREN', 15, 'JUGUETERIA')")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR01', 'TREN', 15, 'JUGUETERIA')")

miConexion.commit()

miConexion.close()