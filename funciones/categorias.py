from configuracion import consultas
from funciones import formato, validaciones


def func_elegir_categoria(actual = None):

    categorias = consultas.func_listar_categorias()

    print()

    func_mostrar_categorias(categorias)

    if not categorias:
        return None

    ids = []

    for categ in categorias:
        ids.append(categ[0])

    print()

    if actual is None:
        mensaje = "ID de la categoria (0 para cancelar): "
        id_actual = None

    else:
        mensaje = f"Cambiar la categoria [{actual[1]}] por (ID): "
        id_actual = actual[0]

    while True:

        id_cat = validaciones.func_pedir_entero(mensaje, 1, 999999999, id_actual)

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




def func_listar_categorias():

    formato.func_limpiar_pantalla()
    print("--- LISTADO DE CATEGORIAS ---\n")
    func_mostrar_categorias(consultas.func_listar_categorias())




def func_pedir_categoria_existente():

    id_cat = func_elegir_categoria()

    if id_cat is None:
        validaciones.func_cancelado()
        return None

    return consultas.func_obtener_categoria(id_cat)




def func_modificar_categoria():

    formato.func_limpiar_pantalla()
    print("--- MODIFICAR CATEGORIA ---")

    categoria = func_pedir_categoria_existente()

    if categoria is None:
        return

    print("\nEnter = dejar el dato actual | 0 = cancelar\n")

    while True:

        mensaje = validaciones.func_mensaje_dato("el nombre", categoria[1])

        nombre = validaciones.func_pedir_texto(mensaje, 50, categoria[1])

        if nombre is None:
            validaciones.func_cancelado()
            return

        if consultas.func_existe_categoria_nombre(nombre, categoria[0]):
            print("Error: Ya existe otra categoria con ese nombre.")
            continue

        break

    consultas.func_actualizar_categoria(categoria[0], nombre)

    print("\nCategoria modificada correctamente.")




def func_nueva_categoria():

    formato.func_limpiar_pantalla()
    print("--- NUEVA CATEGORIA (0 para cancelar) ---\n")

    while True:

        nombre = validaciones.func_pedir_texto(validaciones.func_mensaje_dato("el nombre"), 50)

        if nombre is None:
            validaciones.func_cancelado()
            return

        if consultas.func_existe_categoria_nombre(nombre):
            print("Error: Ya existe una categoria con ese nombre.")
            continue

        break

    consultas.func_insertar_categoria(nombre)

    print("\nCategoria guardada correctamente.")




def func_eliminar_categoria():

    formato.func_limpiar_pantalla()
    print("--- ELIMINAR CATEGORIA ---")

    categoria = func_pedir_categoria_existente()

    if categoria is None:
        return

    cantidad = consultas.func_contar_libros_categoria(categoria[0])

    if cantidad == 1:
        print(f"\nNo se puede eliminar: la categoria [{categoria[1]}], tiene 1 libro asociado.")
        return

    elif cantidad > 1:
        print(f"\nNo se puede eliminar: la categoria [{categoria[1]}], tiene {cantidad} libros asociados.")
        return

    if not validaciones.func_confirmar(f"\nEliminar la categoria [{categoria[1]}]?"):
        validaciones.func_cancelado()
        return

    consultas.func_eliminar_categoria(categoria[0])

    print("\nCategoria eliminada correctamente.")
