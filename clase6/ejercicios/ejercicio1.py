# Lista de números (puede contener duplicados)
numeros = [10, 20, 10, 30, 40, 30, 50]

# Crear un set a partir de la lista
numeros_unicos = set(numeros)
print("Números únicos:", numeros_unicos)

# Valor umbral
umbral = 25

# Contar y almacenar números mayores que el umbral en un nuevo set
mayores_que_umbral = {num for num in numeros_unicos if num > umbral}
print("Números mayores que el umbral:", mayores_que_umbral)
