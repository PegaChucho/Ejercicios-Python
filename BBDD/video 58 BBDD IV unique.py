import sqlite3

miConexion=sqlite3.connect("GestiónProductos")

miCursor=miConexion.cursor()



miConexion.commit()

miConexion.close()