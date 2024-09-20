# Crear el diccionario con información de la clase
clase = {
    'nombre_clase': 'Matemáticas',
    'estudiantes': [
        {'nombre': 'Pedro', 'edad': 15},
        {'nombre': 'Ana', 'edad': 14},
        {'nombre': 'Luis', 'edad': 16}
    ]
}

# Suponemos que conocemos el índice del estudiante a buscar
# Por ejemplo, buscamos a 'Ana', que está en el índice 1
indice = 1
nombre_buscado = 'Ana'
estudiante = clase['estudiantes'][indice]

# Verificar si el nombre coincide
if estudiante['nombre'] == nombre_buscado:
    print(f"La edad de {nombre_buscado} es: {estudiante['edad']}")
else:
    print(f"Estudiante {nombre_buscado} no encontrado")
