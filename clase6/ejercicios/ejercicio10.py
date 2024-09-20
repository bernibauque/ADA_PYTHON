import random

# Generar una lista de números aleatorios entre 1 y 20
numeros = [random.randint(1, 20) for _ in range(10)]
print("Lista de números aleatorios:", numeros)

# Usar un bucle for con range para procesar los números
for numero in numeros:
    if numero < 10:
        continue  # Saltar números menores de 10
    if numero % 15 == 0:
        print(f"Número divisible por 15 encontrado: {numero}. Se detiene la búsqueda.")
        break
    print(f"Número procesado: {numero}")

# Utilizar list comprehension para filtrar los números que no cumplen ninguna condición
filtrados = [num for num in numeros if num >= 10 and num % 15 != 0]
print("Números filtrados:", filtrados)
