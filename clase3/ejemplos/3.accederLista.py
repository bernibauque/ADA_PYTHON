mi_lista = ['a', 'b', 'c', 'd', 'e']

# Acceso por índice:
# Cada elemento en una lista tiene un índice asociado, 
# comenzando desde 0. Puedes acceder a un elemento 
# usando su índice entre corchetes [].
print("Primer elemento:", mi_lista[0])
print("Tercer elemento:", mi_lista[2])

# Acceso por índice negativo
# Los índices negativos permiten acceder a los elementos desde 
# el final de la lista. El índice -1 se refiere al último elemento,
#  -2 al penúltimo, y así sucesivamente.
print("Último elemento:", mi_lista[-1])
print("Penúltimo elemento:", mi_lista[-2])

# Acceso a sublistas (slicing)
# Puedes obtener una sublista utilizando el "slicing" (rebanado) 
# con la notación [inicio:fin]. Esto devuelve una nueva lista que 
# contiene los elementos desde el índice inicio hasta el índice fin-1.
print("Sublista (índice 1 a 3):", mi_lista[1:4])
print("Sublista (inicio a 3):", mi_lista[:3])
print("Sublista (índice 2 a final):", mi_lista[2:])

# Acceso con paso en slicing
# Puedes especificar un paso en la notación de slicing. 
# Esto te permite obtener elementos con un intervalo específico
print("Sublista con paso 2:", mi_lista[::2])
print("Sublista con paso 2 en rango (1 a 4):", mi_lista[1:4:2])

# Iteración a través de la lista
# Puedes usar un bucle for para iterar sobre todos los elementos de la lista.
print("Iteración a través de la lista:")
for elemento in mi_lista:
    print(elemento)

