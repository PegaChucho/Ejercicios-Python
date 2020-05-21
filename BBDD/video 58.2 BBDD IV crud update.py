import sqlite3

miConexion=sqlite3.connect("GestiónProductos")

miCursor=miConexion.cursor()

miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO= 'PELOTA'")


miConexion.commit()

miConexion.close()