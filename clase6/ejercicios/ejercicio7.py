# Inicializar los primeros números de Fibonacci
a, b = 0, 1
fibonacci = []

# Generar la serie de Fibonacci
while a < 100:
    fibonacci.append(a)
    a, b = b, a + b

# Imprimir la serie de Fibonacci
print("Serie de Fibonacci menor a 100:", fibonacci)
