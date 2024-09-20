# Ejemplo Básico de enumerate()
print("Ejemplo Básico de enumerate():")

# Lista de nombres
nombres = ["Ana", "Luis", "Carlos"]

# Usamos enumerate() para obtener el índice y el valor de cada elemento en la lista
# La función enumerate() devuelve un iterador que produce pares (índice, valor)
for indice, nombre in enumerate(nombres):
    # Imprimimos el índice y el nombre usando f-string para una mejor visualización
    print(f"Índice {indice}: {nombre}")

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo Avanzado de enumerate()
print("Ejemplo Avanzado de enumerate():")

# Lista de tareas
tareas = ["Comprar leche", "Ir al gimnasio", "Leer un libro"]

# Usamos una comprensión de lista con enumerate() para numerar las tareas
# Enumeramos la lista 'tareas', donde cada elemento es una tupla (índice, tarea)
# `indice + 1` se usa para empezar la numeración desde 1 en lugar de 0
tareas_numeradas = [f"Tarea {indice + 1}: {tarea}" for indice, tarea in enumerate(tareas)]

# Imprimimos las tareas numeradas
for tarea in tareas_numeradas:
    print(tarea)

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo Avanzado con Índice de Inicio Personalizado
print("Ejemplo Avanzado con Índice de Inicio Personalizado:")

# Lista de tareas con un índice inicial diferente
tareas = ["Comprar leche", "Ir al gimnasio", "Leer un libro"]

# Usamos enumerate() con el parámetro `start` para empezar la numeración en 10
# Esto es útil si necesitas numerar elementos a partir de un número distinto
for indice, tarea in enumerate(tareas, start=10):
    # Imprimimos el índice modificado y la tarea
    print(f"Tarea número {indice}: {tarea}")

print("\n")  # Imprime una línea en blanco para separar los ejemplos

# Ejemplo Avanzado de Enumeración en un Diccionario
print("Ejemplo Avanzado de Enumeración en un Diccionario:")

# Diccionario con claves y valores
productos = {
    "Manzana": 1.5,
    "Banana": 2.0,
    "Cereza": 3.0
}

# Convertimos el diccionario a una lista de pares (ítem, valor) usando items()
# Usamos enumerate() para obtener el índice y los pares (clave, valor)
for indice, (producto, precio) in enumerate(productos.items()):
    # Imprimimos el índice, el producto y el precio
    print(f"Índice {indice}: Producto '{producto}' tiene un precio de ${precio}")

