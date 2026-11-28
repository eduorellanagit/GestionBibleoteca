import os


def func_limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")




def func_lineas_tabla_libros(libros):

    lineas = [
        f"{'ID':<5}{'Titulo':<30}{'Autor':<22}{'ISBN':<7}{'Año':<6}{'Stock':<7}Categoria",
        "-" * 90,
    ]

    for libro in libros:

        lineas.append(
            f"{libro[0]:<5}{func_cortar(libro[1], 28):<30}{func_cortar(libro[2], 20):<22}"
            f"{libro[3]:<7}{libro[4]:<6}{libro[5]:<7}{func_cortar(libro[7], 15)}"
        )

    return lineas




def func_cortar(texto, largo):

    texto = str(texto)
    
    return texto if len(texto) <= largo else texto[:largo - 3] + "..."
