# Crear un set para almacenar los números válidos
numeros_validos = set()

# Iterar sobre los números del 1 al 20
for numero in range(1, 21):
    if numero % 3 == 0:
        continue  # Saltar números divisibles por 3
    if numero > 15:
        break  # Detener si el número es mayor que 15
    numeros_validos.add(numero)

# Verificar si algún número en el set es par
print("Números válidos:", numeros_validos)
for num in numeros_validos:
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
