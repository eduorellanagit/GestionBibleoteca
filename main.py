
from configuracion import conexion
from funciones import categorias, libros, reportes, validaciones

NOMBRE_SISTEMA = "BIBLIOTECA ESCOLAR"

MENU_PRINCIPAL = [

    "Listar libros",
    "Nuevo libro",
    "Modificar libro",
    "Buscar libro",
    "Eliminar libro",
    "Administrar categorias",
    "Reportes"

]

SUBMENU_BUSQUEDA = [

    "Buscar por titulo",
    "Buscar por autor",
    "Buscar por categoria"

]

SUBMENU_CATEGORIAS = [

    "Listar",
    "Nueva",
    "Modificar",
    "Eliminar"

]

SUBMENU_REPORTES = [

    "Ver reporte",
    "Buscar reporte"

]


def main():

    conn = conexion.func_conectar()
    conexion.func_crear_tablas(conn)

    while True:

        opcion = func_mostrar_menu("MENU PRINCIPAL", MENU_PRINCIPAL, "Salir")

        if opcion == 0:
            break

        elif opcion == 1:
            libros.func_listar_libros(conn)

        elif opcion == 2:
            libros.func_nuevo_libro(conn)

        elif opcion == 3:
            libros.func_modificar_libro(conn)

        elif opcion == 4:
            func_submenu_busqueda(conn)
            continue

        elif opcion == 5:
            libros.func_eliminar_libro(conn)

        elif opcion == 6:
            func_submenu_categorias(conn)
            continue

        elif opcion == 7:
            func_submenu_reportes(conn)
            continue

        validaciones.func_pausar()

    conn.close()

    print("\nCerrando. Hasta luego.")


# --- MENU ---

def func_mostrar_menu(titulo, opciones, texto_cero):

    func_mostrar_encabezado(titulo)

    for numero, texto in enumerate(opciones, start=1):
        print(f"{numero}. {texto}")

    print(f"0. {texto_cero} \n")

    return validaciones.func_pedir_opcion(0, len(opciones))


def func_mostrar_encabezado(subtitulo):

    ancho = 60

    print()
    print("*" * ancho)
    print(NOMBRE_SISTEMA.center(ancho))
    print("*" * ancho)

    print(f"\n===== {subtitulo} =====")
    print()


# --- SUBMENUS ---

def func_submenu_busqueda(conn):

    while True:

        opcion = func_mostrar_menu("BUSCAR LIBRO", SUBMENU_BUSQUEDA, "Volver")

        if opcion == 0:
            break

        elif opcion == 1:
            libros.func_buscar_por_titulo(conn)

        elif opcion == 2:
            libros.func_buscar_por_autor(conn)

        elif opcion == 3:
            libros.func_buscar_por_categoria(conn)

        validaciones.func_pausar()


def func_submenu_categorias(conn):

    while True:

        opcion = func_mostrar_menu("SUBMENU CATEGORIAS", SUBMENU_CATEGORIAS, "Volver")

        if opcion == 0:
            break

        elif opcion == 1:
            categorias.func_listar_categorias(conn)

        elif opcion == 2:
            categorias.func_nueva_categoria(conn)

        elif opcion == 3:
            categorias.func_modificar_categoria(conn)

        elif opcion == 4:
            categorias.func_eliminar_categoria(conn)

        validaciones.func_pausar()


def func_submenu_reportes(conn):

    while True:

        opcion = func_mostrar_menu("SUBMENU REPORTES", SUBMENU_REPORTES, "Volver")

        if opcion == 0:
            break

        elif opcion == 1:
            reportes.func_ver_reporte(conn)

        elif opcion == 2:
            reportes.func_buscar_reporte(conn)

        validaciones.func_pausar()


main()
