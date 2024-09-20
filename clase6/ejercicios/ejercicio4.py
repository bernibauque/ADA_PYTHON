# Generar una lista de números del 1 al 10
numeros = list(range(1, 11))

# Usar list comprehension para obtener los cuadrados de números impares
cuadrados_impares = [num**2 for num in numeros if num % 2 != 0]
print("Cuadrados de números impares:", cuadrados_impares)
