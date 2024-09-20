# Crear una lista de diccionarios
estudiantes = [
    {
        'nombre': 'Carlos',
        'edad': 22,
        'calificaciones': [85, 90, 78]
    },
    {
        'nombre': 'Marta',
        'edad': 21,
        'calificaciones': [88, 92, 80]
    }
]

# Imprimir el nombre y las calificaciones del primer estudiante
primer_estudiante = estudiantes[0]
print("Nombre del primer estudiante:", primer_estudiante['nombre'])
print("Calificaciones del primer estudiante:", primer_estudiante['calificaciones'])
