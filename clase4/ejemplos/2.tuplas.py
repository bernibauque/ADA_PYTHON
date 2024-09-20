# Crear una tupla con varios tipos de datos: un número entero, una cadena de texto y un número decimal
tupla_mixta = (1, "Hola", 3.5)

# Mostrar la tupla completa en pantalla
print("Tupla completa:", tupla_mixta)

# Acceder a los elementos de la tupla por su índice (posición)
print("Primer elemento de la tupla:", tupla_mixta[0])  # Imprime: 1
print("Segundo elemento de la tupla:", tupla_mixta[1])  # Imprime: "Hola"
print("Tercer elemento de la tupla:", tupla_mixta[2])  # Imprime: 3.5

# Explicar que las tuplas son inmutables, es decir, no se pueden cambiar sus elementos
print("\nLas tuplas no se pueden modificar. Intentemos cambiar el primer elemento de la tupla:")

# Ejemplo de intento de cambio que causaría un error (no ejecutar esta línea)
# tupla_mixta[0] = 10  # Esto causará un error porque las tuplas no permiten cambios

# Explicación clara de la inmutabilidad
print("Si intentamos hacer 'tupla_mixta[0] = 10',") # un solo print con el de abajo
print("Python mostrará un error porque no se puede cambiar ningún elemento de una tupla.")


# Mostrar cómo podemos "modificar" creando una nueva tupla en vez de intentar cambiar la original
nueva_tupla = (10, "Hola", 3.5)  # Creamos una nueva tupla con el primer valor modificado

# Mostrar la nueva tupla
print("Nueva tupla con el primer elemento cambiado:", nueva_tupla)

# Mostrar que la tupla original permanece igual
print("Tupla original permanece sin cambios:", tupla_mixta)



