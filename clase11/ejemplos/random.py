import random

# Generar un número flotante aleatorio entre 0 y 1
numero_aleatorio = random.random()
print(f"Número aleatorio (0-1): {numero_aleatorio}")

# Generar un número entero aleatorio entre 1 y 10
numero_entero = random.randint(1, 10)
print(f"Número entero aleatorio (1-10): {numero_entero}")

# Seleccionar una fruta al azar de una lista
frutas = ['manzana', 'naranja', 'banana', 'uva', 'pera']
fruta_elegida = random.choice(frutas)
print(f"Fruta elegida: {fruta_elegida}")

# Mezclar aleatoriamente una lista de números
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Números mezclados: {numeros}")

# Generar un número flotante aleatorio entre 5.5 y 10.5
numero_flotante = random.uniform(5.5, 10.5)
print(f"Número flotante aleatorio (5.5-10.5): {numero_flotante}")

# Seleccionar 3 letras al azar de una lista sin repetición
letras = ['a', 'b', 'c', 'd', 'e']
seleccion_letras = random.sample(letras, 3)
print(f"Letras seleccionadas: {seleccion_letras}")
