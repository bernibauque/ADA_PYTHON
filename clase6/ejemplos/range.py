# Ejemplos de uso de range() en Python

# Ejemplo Básico de range()
print("Ejemplo Básico de range():")
for numero in range(5):
    print(numero)

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo con start y stop
print("Ejemplo con start y stop:")
for numero in range(2, 6):
    print(numero)

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo con start, stop y step
print("Ejemplo con start, stop y step:")
for numero in range(1, 11, 2):
    print(numero)

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo con step Negativo
print("Ejemplo con step Negativo:")
for numero in range(10, 0, -1):
    print(numero)

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo Avanzado: Convertir range en una lista
print("Ejemplo Avanzado: Convertir range en una lista:")
numeros = list(range(5))
print(numeros)

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo Avanzado: Crear una Secuencia de Índices para Listas
print("Ejemplo Avanzado: Crear una Secuencia de Índices para Listas:")
frutas = ["manzana", "banana", "cereza"]
for indice in range(len(frutas)):
    print(f"Índice {indice}: {frutas[indice]}")


