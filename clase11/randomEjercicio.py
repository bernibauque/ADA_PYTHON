import random

# Generar un numero flotante aleatorio entre 0 y 1
numero_aleatorio = random.random()
print(f"Numero flotante aleatorio (0-1): {numero_aleatorio}")

# Generar un numero entero aleatorio entre 1 y 10
numero_entero = random.randint(1, 10)
print(f"Numero entero aleatorio (1-10): {numero_entero}")

# Seleccionar una fruta al azar de una lista
fruta = ['manzana', 'naranja', 'banana', 'uva', 'pera']
fruta_elegida = random.choice(fruta)
print(f"Fruta elegida: {fruta_elegida}")

# Mezclar aleatoriamente una lista de numeros
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Numeros mezclados: {numeros}")

# Generar un numero flotante aleatorio entre 5.5 y 10.5
numero_aleatorio2 = random.uniform(5.5, 10.5)
print(f"Numero flotante aleatorio (5.5 - 10.5): {numero_aleatorio2}")

# Seleccionar 3 letras al azar de una lista sin repeticion
letras = ['a', 'b', 'c', 'd', 'e']
seleccion_letras = random.sample(letras, 3)
print(f"Letras seleccionadas: {seleccion_letras}")