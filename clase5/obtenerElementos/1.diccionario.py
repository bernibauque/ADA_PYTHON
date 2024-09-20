# Ejemplo diccionario Vacio
diccionario_vacio = {}
print('Ejemplo diccionario Vacio: ', diccionario_vacio)

# Ejemplo basico de diccionario
diccionario = {
    'nombre': 'María',  # clave es un string, valor es un string
    'edad': 30,         # clave es un string, valor es un entero
    'casado': False,    # clave es un string, valor es un booleano
    'hijos': ['Ana', 'Luis'], # clave es un string, valor es una lista
    'direccion': {      # clave es un string, valor es otro diccionario
        'calle': 'Gran Vía',
        'ciudad': 'Madrid'
    }
}
print('Ejemplo diccionario basico: ', diccionario)

# Ejemplo Diccionario con Valores de Distintos Tipos:
diccionario_mixto = {
    'nombre': 'Carlos',
    1: [2, 4, 3],  # Clave es un entero, valor es una lista
    (2, 3): 'tupla como clave'  # Clave es una tupla, valor es un string
}
print('Ejemplo diccionario mixto: ', diccionario_mixto)

