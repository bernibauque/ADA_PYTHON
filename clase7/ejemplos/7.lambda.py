# Ejemplo 1: Función lambda básica
suma = lambda x, y: x + y
print(f"Suma de 5 + 3: {suma(5, 3)}")  # Imprime 8

# Ejemplo 2: Uso de lambda con map()
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(f"Cuadrados de la lista {numeros}: {list(cuadrados)}")  # Imprime [1, 4, 9, 16, 25]

# Ejemplo 3: Uso de lambda con filter()
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(f"Números pares en {numeros}: {list(pares)}")  # Imprime [2, 4, 6]

# Ejemplo 4: Uso de lambda con sorted()
tuplas = [(1, 2), (3, 1), (5, 0)]
ordenadas = sorted(tuplas, key=lambda t: t[1])
print(f"Lista de tuplas ordenada por el segundo elemento: {ordenadas}")  # Imprime [(5, 0), (3, 1), (1, 2)]

# Ejemplo 5: Uso de lambda con reduce()
from functools import reduce
numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(f"Producto de todos los elementos en {numeros}: {producto}")  # Imprime 24

# Ejemplo 6: Uso de lambda con funciones personalizadas
resta = lambda x, y: x - y
print(f"Resta de 10 - 7: {resta(10, 7)}")  # Imprime 3

# Ejemplo 7: Uso de lambda en funciones integradas (sorted con strings)
nombres = ['Ana', 'Carlos', 'Beatriz', 'David']
ordenados = sorted(nombres, key=lambda nombre: len(nombre))
print(f"Nombres ordenados por longitud: {ordenados}")  # Imprime ['Ana', 'David', 'Carlos', 'Beatriz']
