# Crear el diccionario
libro = {
    'titulo': 'Cien años de soledad',
    'autor': 'Gabriel García Márquez',
    'año': 1967,
    'genero': 'Realismo mágico'
}

# Actualizar el año de publicación
libro['año'] = 1968
print("Después de actualizar el año:", libro)

# Eliminar el género
del libro['genero']
print("Después de eliminar el género:", libro)
