import tkinter as tk
from tkinter import messagebox
import sqlite3


class baseDatos:
    def __init__(self):
        self.miConexion = sqlite3.connect("Usuario")
        self.miCursor = self.miConexion.cursor()

    def crearTabla(self):
        try:
            self.miCursor.execute("""CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR (50),
            PASSWORD VARCHAR (50),
            APELLIDO VARCHAR (20),
            COMENTARIOS VARCHAR (100))""")
            messagebox.showinfo("Completado", "Base creada con éxito")
        except sqlite3.OperationalError:
            return tablaCreada()

    def nuevoDato(self):
        try:
            datos = (datoNombre.guardarDatos(), datoPassword.guardarDatos(), datoApellido.guardarDatos(), datoComentario.guardarDatos())
            if datos == ("", "", "", ""):
                messagebox.showwarning("Error", "Ingresa algún dato para guardar")
                return borrarTodo()
            self.miCursor.execute("""INSERT INTO DATOS_USUARIOS VALUES (
            NULL, ?, ?, ?, ?)""", datos)
            self.miConexion.commit()
            messagebox.showinfo("Dato creado", "El registro fue realizado con éxito.")
            return borrarTodo()

        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Conecta la base de datos en el menu BBDD")

    def editarDato(self):
        try:
            self.miCursor.execute("""UPDATE DATOS_USUARIOS SET
                NOMBRE_USUARIO='{}',
                PASSWORD='{}',
                APELLIDO='{}',
                COMENTARIOS='{}' WHERE ID={}""".format(
                datoNombre.guardarDatos(),
                datoPassword.guardarDatos(),
                datoApellido.guardarDatos(),
                datoComentario.guardarDatos(),
                datoId.guardarDatos()))

            self.miConexion.commit()
            messagebox.showinfo("Actualizado", "Datos actualizados.")
            return borrarTodo()
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ingresa un número de Id o conecta la base de datos en el menu BBDD.")

    def borrarDato(self):
        try:
            self.miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID={}".format(datoId.guardarDatos()))
            self.miConexion.commit()
            messagebox.showinfo("Elimidado", "Datos eliminados.")
            return borrarTodo()

        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ingresa un número de Id o conecta la base de datos en el menu BBDD.")

    def leerDato(self):
        try:
            self.miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID = {}".format(datoId.guardarDatos()))
            datos = self.miCursor.fetchall()

            if datos == []:
                messagebox.showwarning("Dato no encontrado", "Ese id no pertenece a ningún dato, prueba con otro.")
                return borrarTodo()

            for dato in datos:
                datoId.editarDatos(dato[0])
                datoNombre.editarDatos(dato[1])
                datoPassword.editarDatos(dato[2])
                datoApellido.editarDatos(dato[3])
                datoComentario.editarDatos(dato[4])
            self.miConexion.commit()

            return datoId.bloquear()

        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ingresa un número de Id o conecta la base de datos en el menu BBDD.")

    def cerrarBase(self):
        self.miConexion.close()


class dropMenu:
    def __init__(self, master):
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        self.Base = tk.Menu(menubar, tearoff=0)
        self.Base.add_command(label="Conectar", command=base.crearTabla)
        self.Base.add_command(
            label="Salir", command=lambda: self.salida(master))

        self.Borrar = tk.Menu(menubar, tearoff=0)
        self.Borrar.add_command(label="Borrar Todo", command=borrarTodo)

        self.Crud = tk.Menu(menubar, tearoff=0)
        self.Crud.add_command(label="Crear", command=base.nuevoDato)
        self.Crud.add_command(label="Borrar", command=base.borrarDato)
        self.Crud.add_command(label="Actualizar", command=base.editarDato)
        self.Crud.add_command(label="Leer", command=base.leerDato)

        menubar.add_cascade(label="Base", menu=self.Base)
        menubar.add_cascade(label="Borrar", menu=self.Borrar)
        menubar.add_cascade(label="CRUD", menu=self.Crud)

    def salida(self, master):
        a = messagebox.askokcancel("Salir", "¿Quieres salir de la app?")
        if a:
            master.quit()


class dataEntry:
    def __init__(self, master, item, row, caracter=None):
        self.dato = tk.Label(master, text=item)
        self.dato.grid(row=row, column=0, sticky="e")

        self.info = tk.StringVar()

        self.datoEntry = tk.Entry(master, textvariable=self.info, show=caracter)
        self.datoEntry.grid(row=row, column=1)

        if item == "id:" and self.guardarDatos() != "":
            self.datoEntry.config(state="disable")

    def guardarDatos(self):
        self.info.set(self.datoEntry.get())
        dato = self.info.get()
        return dato

    def editarDatos(self, text=""):
        self.info.set(text)
        self.datoEntry.config(state="normal")

    def bloquear(self):
        self.datoEntry.config(state="readonly")


class dataText:
    def __init__(self, master, item, row):
        self.dato = tk.Label(master, text=item)
        self.dato.grid(row=row, column=0, sticky="e")

        self.datoText = tk.Text(master, width=25, height=5)
        self.datoText.grid(row=row, column=1)

        self.scroll = tk.Scrollbar(master, command=self.datoText.yview)
        self.scroll.grid(row=row, column=2, sticky="nse")
        self.datoText.config(yscrollcommand=self.scroll.set)

    def guardarDatos(self, value=None):
        dato = self.datoText.get(1.0, "end-1c")
        return dato

    def editarDatos(self, text=""):
        self.datoText.delete(1.0, "end")
        self.datoText.insert("end", text)


class botonAccion:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.createButton = tk.Button(
            frame, text="Create", command=base.nuevoDato, padx=10)
        self.createButton.pack(side="left", padx=7)

        self.readButton = tk.Button(
            frame, text="Read", command=base.leerDato, padx=10)
        self.readButton.pack(side="left", padx=7)

        self.updateButton = tk.Button(
            frame, text="Update", command=base.editarDato, padx=10)
        self.updateButton.pack(side="left", padx=7)

        self.deleteButton = tk.Button(
            frame, text="Delete", command=base.borrarDato, padx=10)
        self.deleteButton.pack(side="left", padx=7)


def borrarTodo():
    datoId.editarDatos()
    datoNombre.editarDatos()
    datoPassword.editarDatos()
    datoApellido.editarDatos()
    datoComentario.editarDatos()


def tablaCreada():
    messagebox.showwarning("Error de tabla.", "La tabla ya fue creada.")


base = baseDatos()
root = tk.Tk()

frameData = tk.Frame(root)
frameData.pack()

menus = dropMenu(root)

datoId = dataEntry(frameData, "id:", 0,)
datoNombre = dataEntry(frameData, "Nombre de usuario:", 1)
datoPassword = dataEntry(frameData, "Password:", 2, "*")
datoApellido = dataEntry(frameData, "Apellido:", 3)
datoComentario = dataText(frameData, "Comentario:", 4)


botonesCRUD = botonAccion(root)


root.mainloop()
