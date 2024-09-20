# Lista de números predefinida
numeros = [1, 2, 3, 4, 2, 5, 2, 6, 2]

# Pedir al usuario que ingrese un número a buscar
numero_a_buscar = int(input("Ingrese el número a buscar: "))

# Usar el método count() para contar cuántas veces aparece el número
conteo = numeros.count(numero_a_buscar)

# Mostrar el resultado
print(f"El número {numero_a_buscar} aparece {conteo} veces en la lista.")
