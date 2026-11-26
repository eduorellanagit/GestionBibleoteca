from configuracion import consultas
from funciones import validaciones


def func_elegir_categoria(conn):

    categorias = consultas.func_listar_categorias(conn)

    print()

    func_mostrar_categorias(categorias)

    if not categorias:
        return None

    ids = []

    for categ in categorias:
        ids.append(categ[0])

    print()

    while True:

        id_cat = validaciones.func_pedir_entero("ID de la categoria (0 para cancelar): ", 1, 999999999)

        if id_cat is None or id_cat in ids:
            return id_cat

        print("Error: No existe una categoria con ese ID.")




def func_mostrar_categorias(categorias):

    if not categorias:

        print("No hay categorias cargadas.")
        return

    print(f"{'ID':<5}Nombre")
    print("-" * 40)

    for categ in categorias:
        print(f"{categ[0]:<5}{categ[1]}")




def func_listar_categorias(conn):

    print("\n--- LISTADO DE CATEGORIAS ---\n")
    func_mostrar_categorias(consultas.func_listar_categorias(conn))




def func_pedir_categoria_existente(conn):

    id_cat = func_elegir_categoria(conn)

    if id_cat is None:
        validaciones.func_cancelado()
        return None

    return consultas.func_obtener_categoria(conn, id_cat)




def func_modificar_categoria(conn):

    print("\n--- MODIFICAR CATEGORIA ---")

    categoria = func_pedir_categoria_existente(conn)

    if categoria is None:
        return

    while True:

        nombre = validaciones.func_pedir_texto(f"Nuevo nombre [{categoria[1]}] (0 para cancelar): ", 50)

        if nombre is None:
            validaciones.func_cancelado()
            return

        if consultas.func_existe_categoria_nombre(conn, nombre, categoria[0]):
            print("Error: Ya existe otra categoria con ese nombre.")
            continue

        break

    consultas.func_actualizar_categoria(conn, categoria[0], nombre)

    print("\nCategoria modificada correctamente.")




def func_nueva_categoria(conn):

    print("\n--- NUEVA CATEGORIA (0 para cancelar) ---\n")

    while True:

        nombre = validaciones.func_pedir_texto("Nombre: ", 50)

        if nombre is None:
            validaciones.func_cancelado()
            return

        if consultas.func_existe_categoria_nombre(conn, nombre):
            print("Error: Ya existe una categoria con ese nombre.")
            continue

        break

    consultas.func_insertar_categoria(conn, nombre)

    print("\nCategoria guardada correctamente.")




def func_eliminar_categoria(conn):

    print("\n--- ELIMINAR CATEGORIA ---")

    categoria = func_pedir_categoria_existente(conn)

    if categoria is None:
        return

    cantidad = consultas.func_contar_libros_categoria(conn, categoria[0])

    if cantidad == 1:
        print(f"\nNo se puede eliminar: la categoria '{categoria[1]}', tiene 1 libro asociado.")
        return

    elif cantidad > 1:
        print(f"\nNo se puede eliminar: la categoria '{categoria[1]}', tiene {cantidad} libros asociados.")
        return

    if not validaciones.func_confirmar(f"\nEliminar la categoria '{categoria[1]}'?"):
        validaciones.func_cancelado()
        return

    consultas.func_eliminar_categoria(conn, categoria[0])

    print("\nCategoria eliminada correctamente.")
    