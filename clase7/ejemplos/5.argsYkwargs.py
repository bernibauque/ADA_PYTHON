# Ejemplo 1 - función que usa *args
def sumar_numeros(*args):
    """
    Esta función acepta un número variable de argumentos numéricos y retorna su suma.
    :param args: Un número variable de argumentos numéricos.
    :return: La suma de los argumentos.
    """
    total = 0
    for numero in args:
        total += numero
    return total

# Llamada a la función con diferentes números de argumentos
print("Ejemplo de *args:")
print(f"Suma de 1, 2, 3: {sumar_numeros(1, 2, 3)}")          # Output: 6
print(f"Suma de 4, 5, 6, 7, 8: {sumar_numeros(4, 5, 6, 7, 8)}")  # Output: 30
print()

# Ejemplo 2 - función que usa **kwargs
def mostrar_detalles(**kwargs):
    """
    Esta función acepta un número variable de argumentos nombrados (clave-valor) y los imprime.
    :param kwargs: Un número variable de argumentos nombrados (clave-valor).
    """
    print("Detalles:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la función con diferentes argumentos nombrados
print("Ejemplo de **kwargs:")
mostrar_detalles(nombre="Ana", edad=30, ciudad="Madrid")
# Output:
# Detalles:
# nombre: Ana
# edad: 30
# ciudad: Madrid
print()

# Ejemplo 3 - combinado de *args y **kwargs
def mostrar_info_completa(*args, **kwargs):
    """
    Esta función combina argumentos no nombrados y nombrados, y los imprime.
    :param args: Argumentos no nombrados.
    :param kwargs: Argumentos nombrados (clave-valor).
    """
    print("Argumentos no nombrados:")
    for arg in args:
        print(arg)
    
    print("\nArgumentos nombrados:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la función combinada
print("Ejemplo combinado de *args y **kwargs:")
mostrar_info_completa(1, 2, 3, nombre="Ana", edad=30, ciudad="Madrid")


