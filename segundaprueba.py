import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()


def create_table():
    miCursor.execute("""CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    """)

    productos = [
        ("Pelota", 20, "JUGUETERÍA"),
        ("Camisa", 30, "HOMBRES"),
        ("Destornillador", 9, "HERRAMIENTAS"),
        ("Jarrón", 50, "CERÁMICA"),
        ("Pelotas", 15, "JUGUETERÍA")
    ]

    miCursor.executemany(
        'INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)', productos)


def probar():
    miCursor.execute("SELECT * FROM PRODUCTOS")
    productos = miCursor.fetchall()
    for producto in productos:
        print(producto)
    print("-------------------")


def mostrarJuguetes():
    miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='JUGUETERÍA'")
    productos = miCursor.fetchall()
    for producto in productos:
        print(producto)
    print("-------------------")


def actualizarPrecio():
    miCursor.execute(
        "UPDATE PRODUCTOS SET PRECIO=12 WHERE NOMBRE_ARTICULO='Pelota'")


def borrarProducto():
    miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


miConexion.commit()
miConexion.close()
