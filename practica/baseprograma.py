import sqlite3

miConexion = sqlite3.connect("Usuario")
miCursor = miConexion.cursor()


def crearTablas():
    miCursor.execute("""CREATE TABLE DATOS_USUARIOS
    (ID INTEGER PRIMARY KEY AUTOCOMPLEATE,
    NOMBRE_USUARIO VARCHAR (50),
    PASSWORD VARCHAR (50),
    APELLIDO VARCHAR (20),
    COMENTARIOS VARCHAR (100))""")


def nuevoDato():
    pass


def editarDato():
    pass


def borrarDato():
    pass


def leerDato():
    pass


miConexion.close()
