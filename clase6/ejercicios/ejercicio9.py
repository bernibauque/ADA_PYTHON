# Generar una lista de números del 1 al 15
numeros = list(range(1, 16))

# Usar list comprehension para obtener los cubos de los números pares
cubos_pares = [num**3 for num in numeros if num % 2 == 0]
print("Cubos de números pares:", cubos_pares)
