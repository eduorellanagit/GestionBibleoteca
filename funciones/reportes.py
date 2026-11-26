from datetime import datetime

from configuracion import consultas, consultas_reportes
from funciones import formato, validaciones


def func_ver_reporte (conn):

    print("\n--- REPORTE DE LIBROS ---\n")

    libros = consultas.func_listar_libros(conn)

    if not libros:
        print("No hay libros cargados para generar el reporte.")
        return

    total_stock = 0

    for libro in libros:
        total_stock += libro[5]

    ahora = datetime.now()

    print(f"Generado el {ahora:%d/%m/%Y a las %H:%M}\n")

    for linea in formato.func_lineas_tabla_libros(libros):
        print(linea)

    print(f"\nTotal de titulos: {len(libros)}")

    print(f"Total de ejemplares (stock): {total_stock}")

    if not validaciones.func_confirmar("\nGuardar este reporte?"):
        print("\nEl reporte no se guardo.")
        return

    consultas_reportes.func_insertar_reporte (

        conn, ahora.year, ahora.month, f"{ahora:%Y-%m-%d}", f"{ahora:%H:%M}",
        len(libros), total_stock, libros

        )

    print("\nReporte guardado correctamente.")




def func_buscar_reporte (conn):

    print("\n--- BUSCAR REPORTE (0 para cancelar) ---\n")

    anio_actual = datetime.now().year

    anio = validaciones.func_pedir_entero(f"Anio (2000-{anio_actual}): ", 2000, anio_actual)

    if anio is None:
        validaciones.func_cancelado()
        return

    mes = validaciones.func_pedir_entero("Mes (1-12): ", 1, 12)

    if mes is None:
        validaciones.func_cancelado()
        return

    reportes = consultas_reportes.func_buscar_reportes(conn, anio, mes)

    print()

    if not reportes:
        print("No hay reportes guardados en ese periodo.")
        return

    print(f"{'ID':<5}{'Fecha':<13}{'Hora':<8}{'Titulos':<10}Stock")
    print("-" * 45)

    for rep in reportes:
        print(f"{rep[0]:<5}{rep[1]:<13}{rep[2]:<8}{rep[3]:<10}{rep[4]}")

    print()

    reporte = None

    while reporte is None:

        id_rep = validaciones.func_pedir_entero (
            "ID del reporte para ver el detalle (0 para volver): ", 1, 999999999
        )

        if id_rep is None:
            return

        for rep in reportes:

            if rep[0] == id_rep:
                reporte = rep

        if reporte is None:
            print("Error: Ese ID no esta en la lista.")

    func_mostrar_detalle_reporte(conn, reporte)




def func_mostrar_detalle_reporte(conn, reporte):

    print(f"\n--- REPORTE {reporte[0]} ---")
    print(f"Fecha: {reporte[1]}   Hora: {reporte[2]}\n")

    detalle = consultas_reportes.func_listar_detalle_reporte(conn, reporte[0])

    for linea in formato.func_lineas_tabla_libros(detalle):
        print(linea)

    print(f"\nTotal de titulos: {reporte[3]}")
    print(f"Total de ejemplares (stock): {reporte[4]}")
