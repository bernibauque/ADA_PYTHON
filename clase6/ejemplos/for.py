# Programa para imprimir cuadrados de números y calcular la suma

# Definir una lista de números
numeros = [1, 2, 3, 4, 5]

# Inicializar una variable para la suma
suma_cuadrados = 0

# Iterar sobre cada número en la lista
for numero in numeros:
    # Calcular el cuadrado del número
    cuadrado = numero ** 2
    # Imprimir el cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")
    # Agregar el cuadrado a la suma
    suma_cuadrados += cuadrado

# Imprimir la suma de los cuadrados
print(f"La suma de los cuadrados es: {suma_cuadrados}")
