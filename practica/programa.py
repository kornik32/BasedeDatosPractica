""" TODO:
Interfás:
 - 4 Botones menú
    -BBDD/Conectar(Crea una base de datos)
    -BBDD/Salir(Sale de la app)
    -Borrar/Borrar Campos(Limpia los Entry)
    -CRUD/Crear
    -CRUD/Leer
    -CRUD/Actualizar
    -CRUD/Borrar
    -Ayuda/Licencia
    -Ayuda/Acerca de...
Base de datos:
 - ID INT-AUTO
 - NOMBRE_USUARIO 50
 - PASSWORD 50
 - APELLIDO 20
 - DIRECCION 50
 - COMENTARIOS 100"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Base de datos")

menubar = tk.Menu(root)
root.config(menu=menubar)

BBDDs = tk.Menu(menubar, tearoff=0)
BBDDs.add_command(label="Conectar")
BBDDs.add_command(label="Salir")

Borrar = tk.Menu(menubar, tearoff=0)
Borrar.add_command(label="Borrar Campos")

CRUDs = tk.Menu(menubar, tearoff=0)
CRUDs.add_command(label="Crear")
CRUDs.add_command(label="Leer")
CRUDs.add_command(label="Actualizar")
CRUDs.add_command(label="Eliminar")


menubar.add_cascade(label="BBDD", menu=BBDDs)
menubar.add_cascade(label="Borrar", menu=Borrar)
menubar.add_cascade(label="CRUD", menu=CRUDs)
root.mainloop()
