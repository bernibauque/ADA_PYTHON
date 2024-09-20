# Crear el diccionario con anidación
persona = {
    'nombre': 'Laura',
    'edad': 28,
    'direccion': {
        'calle': 'Avenida de la Constitución',
        'ciudad': 'Barcelona',
        'codigo_postal': 08001
    }
}

# Imprimir la ciudad
print("Ciudad:", persona['direccion']['ciudad'])
