
def func_pedir_opcion(minimo, maximo, mensaje = "Opcion: "):

    while True:

        valor = input(mensaje).strip()

        if not (valor.isascii() and valor.isdigit()):

            print("Error: Ingresa solo numeros enteros.")
            continue

        numero = int(valor)

        if numero < minimo or numero > maximo:

            print(f"Error: Elegi una opcion entre {minimo} y {maximo}.")
            continue

        return numero




def func_mensaje_dato(nombre, actual = None, extra = ""):

    if actual is None:
        return f"Ingrese {nombre}{extra}: "

    return f"Cambiar {nombre} [{actual}] por{extra}: "




def func_pedir_texto(mensaje, largo_max = 100, actual = None):

    while True:

        valor = input(mensaje).strip()

        if valor == "" and actual is not None:
            return actual

        if valor == "0":
            return None

        if valor == "":

            print("Error: No puede quedar vacio.")
            continue

        if len(valor) > largo_max:

            print(f"Error: Maximo {largo_max} caracteres.")
            continue

        return valor




def func_pedir_isbn(mensaje, actual = None):

    while True:

        valor = input(mensaje).strip()

        if valor == "" and actual is not None:
            return actual

        if valor == "0":
            return None

        limpio = valor.replace("-", "").replace(" ", "")

        if (limpio.isascii() and limpio.isdigit()) and len(limpio) in (3, 5):
            return limpio

        print("Error: ISBN invalido. Debe tener 3 o 5 digitos (se aceptan guiones).")




def func_pedir_entero(mensaje, minimo, maximo, actual = None):

    while True:

        valor = input(mensaje).strip()

        if valor == "" and actual is not None:
            return actual

        if valor == "0":
            return None

        if not (valor.isascii() and valor.isdigit()):

            print("Error: Ingresa solo numeros enteros.")
            continue

        numero = int(valor)

        if numero < minimo or numero > maximo:

            print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
            continue

        return numero




def func_confirmar(mensaje):

    while True:

        valor = input(f"{mensaje} (s/n): ").strip().lower()

        if valor == "s":
            return True

        if valor == "n":
            return False

        print("Error: Responde 's' o 'n'.")




def func_cancelado():
    print("\nOperacion cancelada.")


def func_pausar():
    input("\nPresiona Enter para continuar...")
