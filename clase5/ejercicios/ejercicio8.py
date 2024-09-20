# Crear el diccionario con información de la tienda
tienda_libros = {
    'nombre_tienda': 'Librería ABC',
    'libros': [
        {'titulo': 'El Quijote', 'precio': 20.50},
        {'titulo': '1984', 'precio': 18.00},
        {'titulo': 'El Principito', 'precio': 12.75}
    ]
}

# Modificar el precio del segundo libro
tienda_libros['libros'][1]['precio'] = 15.99

# Imprimir el título y el precio del segundo libro
segundo_libro = tienda_libros['libros'][1]
print(f"Título del segundo libro: {segundo_libro['titulo']}")
print(f"Precio del segundo libro: {segundo_libro['precio']}")
