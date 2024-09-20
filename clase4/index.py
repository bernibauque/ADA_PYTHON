# Crear una tupla con varios elementos
mi_tupla = (10, 20, 30, 40, 50)

# Encontrar la posicion del numero 30 en la tupla
indice_de_30 = mi_tupla.index(30)

# Mostramos el resultado
print("El numero 30 se encuentra en la posicion ", indice_de_30, " de la tupla.")

# Verificar si un valor esta en tupla antes de buscar su indice
valor_buscado = 60

if valor_buscado in mi_tupla:
    # si el valor esta en la tupla, encontrar su indice
    indice_del_valor = mi_tupla.index(valor_buscado)
    print(f"El numero {valor_buscado} se encuentra en la posicion {indice_del_valor} de la tupla.")
else:
    #Si el valor no esta en la tupla, mostrar un mensaje
    print(f"El numero {valor_buscado} no esta en la tupla.")