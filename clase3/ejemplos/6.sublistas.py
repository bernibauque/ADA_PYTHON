# Definición de una lista
mi_lista = ['a', 'b', 'c', 'd', 'e']

# Obtener una sublista del índice 1 al 4 (exclusivo)
sublista1 = mi_lista[1:4]  # ['b', 'c', 'd']

# Obtener una sublista desde el inicio hasta el índice 3 (exclusivo)
sublista2 = mi_lista[:3]  # ['a', 'b', 'c']

# Obtener una sublista desde el índice 2 hasta el final
sublista3 = mi_lista[2:]  # ['c', 'd', 'e']

# Obtener una sublista con un paso de 2
sublista4 = mi_lista[::2]  # ['a', 'c', 'e']

# Sublista vacía (si el índice de inicio es mayor que el índice de fin)
sublista_vacia = mi_lista[4:2]  # []

print("Sublista (índice 1 a 4):", sublista1)
print("Sublista (inicio a 3):", sublista2)
print("Sublista (índice 2 a final):", sublista3)
print("Sublista con paso 2:", sublista4)
print("Sublista vacía (índice 4 a 2):", sublista_vacia)


