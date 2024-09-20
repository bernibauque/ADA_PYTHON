# Lista para almacenar los números
numeros = []

# Pedir números al usuario
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    numeros.append(numero)

# Calcular la suma usando un bucle for
suma = 0
for num in numeros:
    suma += num

print("La suma de los números ingresados es:", suma)
