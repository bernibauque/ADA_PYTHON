# Crear una tupla con varios elementos
mi_tupla = (10, 20, 30, 40, 50)

# Encontrar la posición del número 30 en la tupla
indice_de_30 = mi_tupla.index(30)

# Mostrar el resultado
print("El número 30 se encuentra en la posición", indice_de_30, "de la tupla.")

# Explicación:
# En la tupla (10, 20, 30, 40, 50), el número 30 está en la posición 2.
# El método index(30) devuelve 2, que es el índice del primer valor 30 en la tupla.

# Verificar si un valor está en la tupla antes de buscar su índice
valor_buscado = 60

if valor_buscado in mi_tupla:
    # Si el valor está en la tupla, encontrar su índice
    indice_del_valor = mi_tupla.index(valor_buscado)
    print(f"El número {valor_buscado} se encuentra en la posición {indice_del_valor} de la tupla.")
else:
    # Si el valor no está en la tupla, mostrar un mensaje
    print(f"El número {valor_buscado} no está en la tupla.")

# Explicación:
# Primero verificamos si el valor 60 está en la tupla usando 'in'.
# Si está, usamos 'index' para encontrar su posición.
# Si no está, mostramos un mensaje indicando que el valor no se encuentra en la tupla.

