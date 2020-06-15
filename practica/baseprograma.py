import sqlite3
from funcionesMenu import tablaCreada

miConexion = sqlite3.connect("Usuario")
miCursor = miConexion.cursor()


def crearTabla():
    try:
        miCursor.execute("""CREATE TABLE DATOS_USUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR (50),
        PASSWORD VARCHAR (50),
        APELLIDO VARCHAR (20),
        COMENTARIOS VARCHAR (100))""")
    except sqlite3.OperationalError:
        return tablaCreada()


def nuevoDato(nombre, passw, apellido, comentarios):
    miCursor.execute("""INSERT INTO DATOS_USUARIOS VALUES (
    NULL, {}, {}, {}, {})""".format(nombre, passw, apellido, comentarios))


def editarDato():
    miCursor.execute("")


def borrarDato():
    pass


def leerDato():
    pass


def cerrarBase():
    miConexion.close()


def probar():
    miCursor.execute("SELECT * FROM DATOS_USUARIOS")
    productos = miCursor.fetchall()
    for producto in productos:
        print(producto)
    print("-------------------")


probar()
