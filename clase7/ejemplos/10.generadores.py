# Ejemplo 1 - Básico de un Generador
# generador que produce números del 1 al 5:
# Definición del generador
def contador():
    # Itera sobre los números del 1 al 5
    for i in range(1, 6): # Itera sobre los números del 1 al 5 (6 no incluido)
        yield i  # Produce el valor de 'i' y pausa la ejecución

# Crear una instancia del generador
gen = contador()  # 'gen' es un objeto generador

# Iterar sobre los valores producidos por el generador
for numero in gen: # Itera sobre cada valor producido por el generador gen.
    print(numero)  # Imprime cada número producido por el generador

# Ejemplo 2 - con Generadores y yield
# Un generador puede tener múltiples yield y puede ser reanudado 
# desde el último yield cada vez que se llama a next():
# Definición del generador para la secuencia de Fibonacci
def fibonacci():
    a, b = 0, 1  # Inicializa los primeros dos números de la secuencia
    while True:  # Ciclo infinito para generar números de Fibonacci
        yield a  # Produce el valor de 'a' y pausa la ejecución
        a, b = b, a + b  # Actualiza 'a' y 'b' para la siguiente iteración

# Crear una instancia del generador
gen = fibonacci()  # 'gen' es un objeto generador que produce números de Fibonacci

# Obtener los primeros 10 números de Fibonacci
for _ in range(10):
    print(next(gen))  # Obtiene el siguiente número en la secuencia y lo imprime

# ¿Qué es la Secuencia de Fibonacci?
# La secuencia de Fibonacci es una serie de números donde cada número es la suma 
# de los dos números anteriores, comenzando típicamente con 0 y 1. La secuencia 
# se ve así: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

