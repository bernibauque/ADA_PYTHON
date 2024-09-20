# Funcion basica lambda
suma = lambda x, y: x + y
print(f"Suma de 5 y 3: {suma(5, 3)}")

# Usando map()
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(f"Cuadrados de la lista: {numeros} : {list(cuadrados)}")

# Usando filter()
numeros2 = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(f"Numero pares en: {numeros2} : {list(pares)}")

# Usando sorted()
tuplas = [(1,2), (3,4), (5,0)]
ordenadas = sorted(tuplas, key=lambda t: t[1])
print(f"Lista de tuplas ordenadas por el segundo elemento: {ordenadas}")



