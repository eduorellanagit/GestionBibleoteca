from configuracion import consultas
from funciones import formato, validaciones


def func_elegir_autor(actual = None):

    autores = consultas.func_listar_autores()

    print()

    func_mostrar_autores(autores)

    if not autores:
        return None

    ids = []

    for autor in autores:
        ids.append(autor[0])

    print()

    if actual is None:
        mensaje = "ID del autor (0 para cancelar): "
        id_actual = None

    else:
        mensaje = f"Cambiar el autor [{actual[1]}] por (ID): "
        id_actual = actual[0]

    while True:

        id_autor = validaciones.func_pedir_entero(mensaje, 1, 999999999, id_actual)

        if id_autor is None or id_autor in ids:
            return id_autor

        print("Error: No existe un autor con ese ID.")




def func_mostrar_autores(autores):

    if not autores:

        print("No hay autores cargados.")
        return

    print(f"{'ID':<5}Nombre")
    print("-" * 40)

    for autor in autores:
        print(f"{autor[0]:<5}{autor[1]}")




def func_listar_autores():

    formato.func_limpiar_pantalla()
    print("--- LISTADO DE AUTORES ---\n")
    func_mostrar_autores(consultas.func_listar_autores())




def func_pedir_autor_existente():

    id_autor = func_elegir_autor()

    if id_autor is None:
        validaciones.func_cancelado()
        return None

    return consultas.func_obtener_autor(id_autor)




def func_modificar_autor():

    formato.func_limpiar_pantalla()
    print("--- MODIFICAR AUTOR ---")

    autor = func_pedir_autor_existente()

    if autor is None:
        return

    print("\nEnter = dejar el dato actual | 0 = cancelar\n")

    while True:

        mensaje = validaciones.func_mensaje_dato("el nombre", autor[1])

        nombre = validaciones.func_pedir_texto(mensaje, 80, autor[1])

        if nombre is None:
            validaciones.func_cancelado()
            return

        if consultas.func_existe_autor_nombre(nombre, autor[0]):
            print("Error: Ya existe otro autor con ese nombre.")
            continue

        break

    consultas.func_actualizar_autor(autor[0], nombre)

    print("\nAutor modificado correctamente.")




def func_nuevo_autor():

    formato.func_limpiar_pantalla()
    print("--- NUEVO AUTOR (0 para cancelar) ---\n")

    while True:

        nombre = validaciones.func_pedir_texto(validaciones.func_mensaje_dato("el nombre"), 80)

        if nombre is None:
            validaciones.func_cancelado()
            return

        if consultas.func_existe_autor_nombre(nombre):
            print("Error: Ya existe un autor con ese nombre.")
            continue

        break

    consultas.func_insertar_autor(nombre)

    print("\nAutor guardado correctamente.")




def func_eliminar_autor():

    formato.func_limpiar_pantalla()
    print("--- ELIMINAR AUTOR ---")

    autor = func_pedir_autor_existente()

    if autor is None:
        return

    cantidad = consultas.func_contar_libros_autor(autor[0])

    if cantidad == 1:
        print(f"\nNo se puede eliminar: el autor [{autor[1]}], tiene 1 libro asociado.")
        return

    elif cantidad > 1:
        print(f"\nNo se puede eliminar: el autor [{autor[1]}], tiene {cantidad} libros asociados.")
        return

    if not validaciones.func_confirmar(f"\nEliminar el autor [{autor[1]}]?"):
        validaciones.func_cancelado()
        return

    consultas.func_eliminar_autor(autor[0])

    print("\nAutor eliminado correctamente.")
