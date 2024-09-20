# Crear un diccionario con información de una persona
persona = {
    'nombre': 'Ana',
    'edad': 30,
    'ciudad': 'Madrid'
}

# Usar .pop() para eliminar el elemento con la clave 'edad' y obtener su valor
valor_eliminado = persona.pop('edad')

# Imprimir el valor eliminado y el diccionario resultante
print("Valor eliminado:", valor_eliminado)  # Output: 30
print("Diccionario después de eliminar 'edad':", persona)  # Output: {'nombre': 'Ana', 'ciudad': 'Madrid'}

# Usar .pop() con una clave que no existe y un valor por defecto
valor_inexistente = persona.pop('pais', 'No especificado')
print("Valor cuando la clave no existe:", valor_inexistente)  # Output: No especificado

# Intentar usar .pop() sin valor por defecto en una clave que no existe
# Esto lanzará un KeyError
try:
    persona.pop('pais')  # 'pais' no está en el diccionario y no se ha dado un valor por defecto
except KeyError as e:
    print(f"Error: {e} - La clave no existe en el diccionario.")
