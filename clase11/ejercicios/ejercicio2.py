import random

# Simular el lanzamiento de un dado (5 veces)
print("Lanzamiento de un dado:")
for i in range(5):
    dado = random.randint(1, 6)
    print(f"Lanzamiento {i+1}: {dado}")

# Generar una lista de 10 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print("\nLista de 10 números aleatorios:")
print(numeros_aleatorios)

# Seleccionar aleatoriamente un número de la lista generada
seleccionado = random.choice(numeros_aleatorios)
print(f"\nNúmero seleccionado aleatoriamente de la lista: {seleccionado}")
