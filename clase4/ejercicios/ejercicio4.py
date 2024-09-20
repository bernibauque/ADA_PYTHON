# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
# Consigna:

# Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
# Usa el método index para encontrar la posición de la fruta "banana".
# Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.

# Crear la tupla
frutas = ("manzana", "banana", "cereza")

# Encontrar la posición de "banana"
indice_banana = frutas.index("banana")
print("La fruta 'banana' se encuentra en la posición", indice_banana, "de la tupla.")

# Verificar si "naranja" está en la tupla
if "naranja" in frutas:
    print("La fruta 'naranja' está en la tupla.")
else:
    print("La fruta 'naranja' no está en la tupla.")
