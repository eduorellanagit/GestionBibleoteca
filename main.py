from configuracion import conexion
from funciones import autores, categorias, formato, libros, reportes, validaciones

NOMBRE_SISTEMA = "BIBLIOTECA ESCOLAR"

MENU_PRINCIPAL = [

    "Listar Libros",
    "Nuevo Libro",
    "Modificar Libro",
    "Buscar Libro",
    "Eliminar Libro",
    "Administrar Categorias",
    "Administrar Autores",
    "Reportes de Libros"

]

SUBMENU_LISTADO = [

    "Listar Libros por ID",
    "Listar Libros por Titulo",
    "Listar Libros por Año",
    "Listar Libros por Autor"

]

SUBMENU_BUSQUEDA = [

    "Buscar Libro por Titulo",
    "Buscar Libro por Autor",
    "Buscar Libro por Categoria"

]

SUBMENU_CATEGORIAS = [

    "Listar Categorias",
    "Nueva Categoria",
    "Modificar Categoria",
    "Eliminar Categoria"

]

SUBMENU_AUTORES = [

    "Listar Autores",
    "Nuevo Autor",
    "Modificar Autor",
    "Eliminar Autor"

]

SUBMENU_REPORTES = [

    "Ver Reporte de Libros",
    "Buscar Reportes Guardados"

]


def main():

    conexion.func_conectar()
    conexion.func_crear_tablas()

    while True:

        opcion = func_mostrar_menu("MENU PRINCIPAL", MENU_PRINCIPAL, "Salir del Programa")

        match opcion:

            case 0:
                break

            case 1:
                func_submenu_listado()
                continue

            case 2:
                libros.func_nuevo_libro()

            case 3:
                libros.func_modificar_libro()

            case 4:
                func_submenu_busqueda()
                continue

            case 5:
                libros.func_eliminar_libro()

            case 6:
                func_submenu_categorias()
                continue

            case 7:
                func_submenu_autores()
                continue
            
            case 8:
                func_submenu_reportes()
                continue

        validaciones.func_pausar()

    conexion.func_cerrar()

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

    formato.func_limpiar_pantalla()

    print("*" * ancho)
    print(NOMBRE_SISTEMA.center(ancho))
    print("*" * ancho)

    print(f"\n===== {subtitulo} =====")
    print()


# --- SUBMENUS ---

def func_submenu_listado():

    while True:

        opcion = func_mostrar_menu("LISTAR LIBROS (ORDENAR)", SUBMENU_LISTADO, "Volver al Menu Principal")

        match opcion:

            case 0:
                break
            case _:
                libros.func_listar_libros(opcion)

        validaciones.func_pausar()


def func_submenu_busqueda():

    while True:

        opcion = func_mostrar_menu("BUSCAR LIBRO", SUBMENU_BUSQUEDA, "Volver al Menu Principal")

        match opcion:

            case 0:
                break

            case 1:
                libros.func_buscar_por_titulo()

            case 2:
                libros.func_buscar_por_autor()

            case 3:
                libros.func_buscar_por_categoria()

        validaciones.func_pausar()


def func_submenu_categorias():

    while True:

        opcion = func_mostrar_menu("SUBMENU CATEGORIAS", SUBMENU_CATEGORIAS, "Volver al Menu Principal")

        match opcion:

            case 0:
                break

            case 1:
                categorias.func_listar_categorias()

            case 2:
                categorias.func_nueva_categoria()

            case 3:
                categorias.func_modificar_categoria()

            case 4:
                categorias.func_eliminar_categoria()

        validaciones.func_pausar()


def func_submenu_autores():

    while True:

        opcion = func_mostrar_menu("SUBMENU AUTORES", SUBMENU_AUTORES, "Volver al Menu Principal")

        match opcion:

            case 0:
                break

            case 1:
                autores.func_listar_autores()

            case 2:
                autores.func_nuevo_autor()

            case 3:
                autores.func_modificar_autor()

            case 4:
                autores.func_eliminar_autor()

        validaciones.func_pausar()


def func_submenu_reportes():

    while True:

        opcion = func_mostrar_menu("SUBMENU REPORTES", SUBMENU_REPORTES, "Volver al Menu Principal")

        match opcion:

            case 0:
                break

            case 1:
                reportes.func_ver_reporte()

            case 2:
                reportes.func_buscar_reporte()

        validaciones.func_pausar()


main()
