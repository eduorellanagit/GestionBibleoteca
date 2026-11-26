from datetime import date

from configuracion import consultas
from funciones import categorias, formato, validaciones


def func_listar_libros(conn):

    print("\n--- LISTADO DE LIBROS ---\n")
    func_mostrar_libros(consultas.func_listar_libros(conn))




def func_mostrar_libros(libros):

    if not libros:
        print("No se encontraron libros.")
        return

    for linea in formato.func_lineas_tabla_libros(libros):
        print(linea)

    if len(libros) == 1:
        print("\nTotal: 1 libro")

    else:
        print(f"\nTotal: {len(libros)} libros")




def func_nuevo_libro(conn):

    print("\n--- NUEVO LIBRO (0 para cancelar en cualquier momento) ---")

    if not consultas.func_listar_categorias(conn):
        print("\nPrimero tenes que crear al menos una categoria en Administrar categorias.")
        return

    datos = func_pedir_datos_libro(conn)

    if datos is None:
        validaciones.func_cancelado()
        return

    titulo, autor, isbn, anio, stock, id_cat = datos

    consultas.func_insertar_libro(conn, titulo, autor, isbn, anio, stock, id_cat)

    print("\nExito: Libro guardado correctamente.")




def func_modificar_libro(conn):

    print("\n--- MODIFICAR LIBRO ---")

    libro = func_pedir_libro_existente(conn)

    if libro is None:
        return

    print("\nIngresa los nuevos datos (0 para cancelar, no se guarda nada)")

    datos = func_pedir_datos_libro(conn, libro[0])

    if datos is None:
        validaciones.func_cancelado()
        return

    titulo, autor, isbn, anio, stock, id_cat = datos

    consultas.func_actualizar_libro(conn, libro[0], titulo, autor, isbn, anio, stock, id_cat)

    print("\nLibro modificado correctamente.")




def func_pedir_datos_libro(conn, id_libro = 0):

    titulo = validaciones.func_pedir_texto("\nTitulo: ", 100)

    if titulo is None:
        return None

    autor = validaciones.func_pedir_texto("Autor: ", 80)

    if autor is None:
        return None

    while True:

        isbn = validaciones.func_pedir_isbn("ISBN (10 o 13 digitos): ")

        if isbn is None:
            return None

        if consultas.func_existe_isbn(conn, isbn, id_libro):
            print("Error: Ya existe un libro con ese ISBN.")
            continue

        break

    anio_actual = date.today().year

    anio = validaciones.func_pedir_entero(f"Anio de publicacion (1000-{anio_actual}): ", 1000, anio_actual)

    if anio is None:
        return None

    stock = validaciones.func_pedir_entero("Stock (1-999): ", 1, 999)

    if stock is None:
        return None

    id_cat = categorias.func_elegir_categoria(conn)

    if id_cat is None:
        return None

    return titulo, autor, isbn, anio, stock, id_cat




def func_pedir_libro_existente(conn):

    libros = consultas.func_listar_libros(conn)

    print()

    if not libros:
        print("No hay libros cargados.")
        return None

    func_mostrar_libros(libros)

    print()

    while True:

        id_libro = validaciones.func_pedir_entero("ID del libro (0 para cancelar): ", 1, 999999999)

        if id_libro is None:
            validaciones.func_cancelado()
            return None

        libro = consultas.func_obtener_libro(conn, id_libro)

        if libro is not None:
            return libro

        print("Error: No existe un libro con ese ID.")




def func_eliminar_libro(conn):

    print("\n--- ELIMINAR LIBRO ---")

    libro = func_pedir_libro_existente(conn)

    if libro is None:
        return

    if not validaciones.func_confirmar(f"\nEliminar el libro '{libro[1]}' de {libro[2]}?"):
        validaciones.func_cancelado()
        return

    consultas.func_eliminar_libro(conn, libro[0])

    print("\nLibro eliminado correctamente.")




# --- BUSQUEDAS ---

def func_buscar_por_titulo(conn):

    print("\n--- BUSCAR POR TITULO ---\n")

    texto = validaciones.func_pedir_texto("Texto a buscar (0 para cancelar): ", 100)

    if texto is None:
        validaciones.func_cancelado()
        return

    print()

    func_mostrar_libros(consultas.func_buscar_libros_por_titulo(conn, texto))




def func_buscar_por_autor(conn):

    print("\n--- BUSCAR POR AUTOR ---\n")

    texto = validaciones.func_pedir_texto("Texto a buscar (0 para cancelar): ", 80)

    if texto is None:
        validaciones.func_cancelado()
        return

    print()

    func_mostrar_libros(consultas.func_buscar_libros_por_autor(conn, texto))




def func_buscar_por_categoria(conn):

    print("\n--- BUSCAR POR CATEGORIA ---")

    id_cat = categorias.func_elegir_categoria(conn)

    if id_cat is None:
        validaciones.func_cancelado()
        return

    print()

    func_mostrar_libros(consultas.func_buscar_libros_por_categoria(conn, id_cat))

