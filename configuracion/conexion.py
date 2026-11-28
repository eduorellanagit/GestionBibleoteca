import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_BD = os.path.join(BASE_DIR, "biblioteca.db")


conn = None


def func_conectar():

    global conn

    conn = sqlite3.connect(RUTA_BD)
    conn.execute("PRAGMA foreign_keys = ON")




def func_cerrar():
    conn.close()




def func_crear_tablas():

    conn.execute("""
        CREATE TABLE IF NOT EXISTS t_categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )""")


    conn.execute("""
        CREATE TABLE IF NOT EXISTS t_autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )""")


    conn.execute("""
        CREATE TABLE IF NOT EXISTS t_libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            id_autor INTEGER NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            anio INTEGER NOT NULL,
            stock INTEGER NOT NULL DEFAULT 1,
            id_categoria INTEGER NOT NULL,
            FOREIGN KEY (id_autor) REFERENCES t_autores(id),
            FOREIGN KEY (id_categoria) REFERENCES t_categorias(id)
        )""")


    conn.execute("""
        CREATE TABLE IF NOT EXISTS t_reportes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            anio INTEGER NOT NULL,
            mes INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            total_titulos INTEGER NOT NULL,
            total_stock INTEGER NOT NULL
        )""")


    conn.execute("""
        CREATE TABLE IF NOT EXISTS t_reportes_detalle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_reporte INTEGER NOT NULL,
            id_libro INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            isbn TEXT NOT NULL,
            anio_publicacion INTEGER NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL,
            FOREIGN KEY (id_reporte) REFERENCES t_reportes(id)
        )""")


    conn.commit()
