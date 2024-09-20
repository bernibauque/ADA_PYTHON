# Definimos una matriz de 3x3
matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]

# Acceder y mostrar algunos elementos específicos de la matriz
print("Algunos elementos de la matriz:")
print("Elemento en fila 0, columna 0:", matriz[0][0])  # Elemento en fila 0, columna 0 (1)
print("Elemento en fila 1, columna 2:", matriz[1][2])  # Elemento en fila 1, columna 2 (6)

# Modificar elementos específicos de la matriz
print("\nModificando elementos específicos:")
matriz[0][1] = 10  # Cambiar el elemento en fila 0, columna 1 a 10
matriz[2][0] = 15  # Cambiar el elemento en fila 2, columna 0 a 15
print("Matriz después de las modificaciones:")
print(matriz)  # Imprime la matriz completa después de las modificaciones

# Acceder a una fila completa
print("\nAccediendo a una fila completa:")
fila_completa = matriz[1]  # Obtener toda la segunda fila
print("Fila completa en la posición 1:", fila_completa)  # Imprime [4, 5, 6]

# Reemplazar una fila completa
print("\nReemplazando una fila completa:")
matriz[1] = [20, 21, 22]  # Reemplazar la segunda fila con nuevos valores
print("Matriz después de reemplazar la fila 1:")
print(matriz)  # Imprime la matriz completa después de reemplazar la fila

# Trabajar con una submatriz (parte de la matriz)
print("\nTrabajando con una submatriz:")
submatriz = [matriz[0][1:3], matriz[1][1:3]]  # Extraer submatriz de las columnas 1 a 2 de las filas 0 y 1
print("Submatriz extraída:", submatriz)  # Imprime [[10, 3], [21, 22]]

# Mostrar toda la matriz al final
print("\nMatriz completa al final:")
print(matriz[0])  # Imprime la primera fila
print(matriz[1])  # Imprime la segunda fila
print(matriz[2])  # Imprime la tercera fila

