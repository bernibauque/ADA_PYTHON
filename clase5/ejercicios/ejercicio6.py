# Crear el diccionario con anidación
escuela = {
    'nombre': 'Escuela Primaria Ejemplo',
    'año_fundacion': 1995,
    'clases': [
        {
            'nombre_clase': 'Matemáticas',
            'estudiantes': [
                {'nombre': 'Pedro', 'edad': 10},
                {'nombre': 'Ana', 'edad': 11}
            ]
        },
        {
            'nombre_clase': 'Ciencias',
            'estudiantes': [
                {'nombre': 'Luis', 'edad': 12},
                {'nombre': 'María', 'edad': 11}
            ]
        }
    ]
}

# Imprimir el nombre del primer estudiante de la primera clase
primer_estudiante_clase1 = escuela['clases'][0]['estudiantes'][0]
print("Nombre del primer estudiante de la primera clase:", primer_estudiante_clase1['nombre'])
