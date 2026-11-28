from datetime import date

from configuracion import consultas
from funciones import autores, categorias, formato, validaciones


def func_listar_libros(opcion = 2):

    formato.func_limpiar_pantalla()
    print("--- LISTADO DE LIBROS ---\n")
    func_mostrar_libros(consultas.func_listar_libros(opcion))




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




def func_nuevo_libro():

    formato.func_limpiar_pantalla()
    print("--- NUEVO LIBRO (0 para cancelar en cualquier momento) ---")

    if not consultas.func_listar_categorias():
        print("\nPrimero tenes que crear al menos una categoria en Administrar categorias.")
        return

    if not consultas.func_listar_autores():
        print("\nPrimero tenes que crear al menos un autor en Administrar autores.")
        return

    datos = func_pedir_datos_libro()

    if datos is None:
        validaciones.func_cancelado()
        return

    titulo, id_autor, isbn, anio, stock, id_cat = datos

    consultas.func_insertar_libro(titulo, id_autor, isbn, anio, stock, id_cat)

    print("\nExito: Libro guardado correctamente.")




def func_modificar_libro():

    formato.func_limpiar_pantalla()
    print("--- MODIFICAR LIBRO ---")

    libro = func_pedir_libro_existente()

    if libro is None:
        return

    print("\nEnter = dejar el dato actual | 0 = cancelar (no se guarda nada)")

    datos = func_pedir_datos_libro(libro)

    if datos is None:
        validaciones.func_cancelado()
        return

    titulo, id_autor, isbn, anio, stock, id_cat = datos

    consultas.func_actualizar_libro(libro[0], titulo, id_autor, isbn, anio, stock, id_cat)

    print("\nLibro modificado correctamente.")




def func_pedir_datos_libro(libro = None):

    if libro is None:

        id_libro = 0
        titulo_act = None
        autor_act = None
        isbn_act = None
        anio_act = None
        stock_act = None
        cat_act = None

    else:

        id_libro = libro[0]
        titulo_act = libro[1]
        autor_act = (libro[8], libro[2])
        isbn_act = libro[3]
        anio_act = libro[4]
        stock_act = libro[5]
        cat_act = (libro[6], libro[7])

    print()

    mensaje = validaciones.func_mensaje_dato("el titulo", titulo_act)

    titulo = validaciones.func_pedir_texto(mensaje, 100, titulo_act)

    if titulo is None:
        return None

    id_autor = autores.func_elegir_autor(autor_act)

    if id_autor is None:
        return None

    print()

    while True:

        mensaje = validaciones.func_mensaje_dato("el ISBN", isbn_act, " (3 o 5 digitos)")

        isbn = validaciones.func_pedir_isbn(mensaje, isbn_act)

        if isbn is None:
            return None

        if consultas.func_existe_isbn(isbn, id_libro):
            print("Error: Ya existe un libro con ese ISBN.")
            continue

        break

    anio_actual = date.today().year

    mensaje = validaciones.func_mensaje_dato("el año", anio_act, f" (868-{anio_actual})")

    # El primer libro impreso conocido de la historia es el Sutra del Diamante,
    # que fue creado oficialmente el 11 de mayo de 868 d.C. en China mediante xilografía. Segun Google

    anio = validaciones.func_pedir_entero(mensaje, 868, anio_actual, anio_act)

    if anio is None:
        return None

    mensaje = validaciones.func_mensaje_dato("el stock", stock_act, " (1-200)")

    stock = validaciones.func_pedir_entero(mensaje, 1, 200, stock_act)

    if stock is None:
        return None

    id_cat = categorias.func_elegir_categoria(cat_act)

    if id_cat is None:
        return None

    return titulo, id_autor, isbn, anio, stock, id_cat




def func_pedir_libro_existente():

    libros = consultas.func_listar_libros()

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

        libro = consultas.func_obtener_libro(id_libro)

        if libro is not None:
            return libro

        print("Error: No existe un libro con ese ID.")




def func_eliminar_libro():

    formato.func_limpiar_pantalla()
    print("--- ELIMINAR LIBRO ---")

    libro = func_pedir_libro_existente()

    if libro is None:
        return

    if not validaciones.func_confirmar(f"\nEliminar el libro [{libro[1]}] de [{libro[2]}]?"):
        validaciones.func_cancelado()
        return

    consultas.func_eliminar_libro(libro[0])

    print("\nLibro eliminado correctamente.")




# --- BUSQUEDAS ---

def func_buscar_por_titulo():

    formato.func_limpiar_pantalla()
    print("--- BUSCAR POR TITULO ---\n")

    texto = validaciones.func_pedir_texto("Texto a buscar (0 para cancelar): ", 100)

    if texto is None:
        validaciones.func_cancelado()
        return

    print()

    func_mostrar_libros(consultas.func_buscar_libros_por_titulo(texto))




def func_buscar_por_autor():

    formato.func_limpiar_pantalla()
    print("--- BUSCAR POR AUTOR ---")

    id_autor = autores.func_elegir_autor()

    if id_autor is None:
        validaciones.func_cancelado()
        return

    print()

    func_mostrar_libros(consultas.func_buscar_libros_por_autor(id_autor))




def func_buscar_por_categoria():

    formato.func_limpiar_pantalla()
    print("--- BUSCAR POR CATEGORIA ---")

    id_cat = categorias.func_elegir_categoria()

    if id_cat is None:
        validaciones.func_cancelado()
        return

    print()

    func_mostrar_libros(consultas.func_buscar_libros_por_categoria(id_cat))
