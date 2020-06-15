import tkinter as tk
import sqlite3
from funcionesMenu import *

#  Creamos la ventana principal
root = tk.Tk()
root.title("Base de datos")

#  --------------------------BaseDeDatos---------------------

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
        miConexion.commit()
    except sqlite3.OperationalError:
        return tablaCreada()


def nuevoDato(nombre, passw, apellido, comentarios, id):
    miCursor.execute(
        "INSERT INTO DATOS_USUARIOS VALUES(NULL,'{}','{}','{}','{}')"
        .format(nombre, passw, apellido, comentarios))
    miCursor.execute("SELECT * FROM DATOS_USUARIOS")
    miConexion.commit()
    return borrarTodo(id, nombre, passw, apellido)


def editarDato():
    miCursor.execute("")


def borrarDato():
    pass


def leerDato():
    pass


def cerrarBase():
    miConexion.close()


# ------------------------Display FRAME---------------------
id = tk.IntVar()
nombre = tk.StringVar()
passw = tk.StringVar()
apell = tk.StringVar()
come = tk.StringVar()

mainframe = tk.Frame(root)
mainframe.pack()

tk.Label(mainframe, text="id").grid(row=0, column=1)
idE = tk.Entry(mainframe, textvariable=id, text="")
idE.grid(row=0, column=2)
if id == "":
    idE.config(state="disable")


tk.Label(mainframe, text="Nombre de usuario").grid(row=1, column=1)
nomE = tk.Entry(mainframe, textvariable=nombre)
nomE.grid(row=1, column=2)

tk.Label(mainframe, text="Password").grid(row=2, column=1)
passE = tk.Entry(mainframe, textvariable=passw)
passE.grid(row=2, column=2)
passE.config(show="*")

tk.Label(mainframe, text="Apellido").grid(row=3, column=1)
apeE = tk.Entry(mainframe, textvariable=apell)
apeE.grid(row=3, column=2)

tk.Label(mainframe, text="Comentarios").grid(row=4, column=1)
comE = tk.Text(mainframe)
comE.config(width=26, height=3)
comE.grid(row=4, column=2)

#  ----------------------------Botones---------------------------

buttonFrame = tk.Frame(mainframe)
buttonFrame.grid(row=5, columnspan=3)


def nuevaEntrada():
    nombre.set(nomE.get())
    passw.set(passE.get())
    apell.set(apeE.get())
    come.set(comE.get("1.0", "end-1c"))
    a = nombre.get()
    b = passw.get()
    c = apell.get()
    d = come.get()
    return nuevoDato(a, b, c, d, id)


tk.Button(buttonFrame, text="Crear", command=nuevaEntrada).grid(row=5, column=0, padx=10)
tk.Button(buttonFrame, text="Leer").grid(row=5, column=1, padx=10)
tk.Button(buttonFrame, text="Actualizar").grid(row=5, column=2, padx=10)
tk.Button(buttonFrame, text="Eliminar").grid(row=5, column=3, padx=10)

#  -------------------Display Menu-----------------------------
menubar = tk.Menu(root)
root.config(menu=menubar)

BBDDs = tk.Menu(menubar, tearoff=0)
BBDDs.add_command(label="Conectar", command=crearTabla)
BBDDs.add_command(label="Salir", command=lambda: salida(root))

Borrar = tk.Menu(menubar, tearoff=0)
Borrar.add_command(label="Borrar Campos", command=lambda: borrarTodo(id,
                   nombre, passw, apell))

CRUDs = tk.Menu(menubar, tearoff=0)
CRUDs.add_command(label="Crear")
CRUDs.add_command(label="Leer")
CRUDs.add_command(label="Actualizar")
CRUDs.add_command(label="Eliminar")


menubar.add_cascade(label="BBDD", menu=BBDDs)
menubar.add_cascade(label="Borrar", menu=Borrar)
menubar.add_cascade(label="CRUD", menu=CRUDs)


root.mainloop()
