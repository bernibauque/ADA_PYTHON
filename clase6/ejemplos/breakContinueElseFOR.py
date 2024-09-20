# Lista de números para buscar
numeros = [7, -2, 5, -1, 3, 9, 4]
# Número objetivo que queremos encontrar
objetivo = 3

# Bucle para buscar el número objetivo
for numero in numeros:
    if numero < 0:
        # Si el número es negativo, saltar a la siguiente iteración
        continue
    if numero == objetivo:
        # Si encontramos el número objetivo, salir del bucle
        print(f"Número objetivo {objetivo} encontrado.")
        break
else:
    # Este bloque se ejecuta solo si no se encuentra el número objetivo
    print(f"Número objetivo {objetivo} no encontrado en la lista.")





