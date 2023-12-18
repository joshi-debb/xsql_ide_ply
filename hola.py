def es_entero(cadena):
    return cadena.isdigit()

def es_flotante(cadena):
    try:
        float_cadena = float(cadena)
        return True
    except ValueError:
        return False

# Ejemplos
cadena_entero = "123"
cadena_flotante = "123.45"
cadena_no_numero = "abc"

if es_entero(cadena_entero):
    print(f"{cadena_entero} es un número entero.")
else:
    print(f"{cadena_entero} no es un número entero.")

if es_flotante(cadena_flotante):
    print(f"{cadena_flotante} es un número flotante.")
else:
    print(f"{cadena_flotante} no es un número flotante.")

if es_flotante(cadena_no_numero):
    print(f"{cadena_no_numero} es un número flotante.")
else:
    print(f"{cadena_no_numero} no es un número flotante.")