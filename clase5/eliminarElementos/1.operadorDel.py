# Crear un diccionario con información de un estudiante
estudiante = {
    "nombre": "Laura",
    "edad": 22,
    "curso": "Ingeniería",
    "ciudad": "Valencia"
}

# Imprimir el diccionario original
print("Diccionario original:", estudiante)

# Eliminar el elemento con la clave 'curso' usando el operador del
del estudiante["curso"]

# Imprimir el diccionario después de eliminar 'curso'
print("Diccionario después de eliminar 'curso':", estudiante)

# Eliminar el elemento con la clave 'ciudad'
del estudiante["ciudad"]

# Imprimir el diccionario después de eliminar 'ciudad'
print("Diccionario después de eliminar 'ciudad':", estudiante)

# Intentar eliminar una clave que no existe para ver qué pasa
# Esto lanzará un KeyError
try:
    del estudiante["pais"]  # Clave 'pais' no existe
except KeyError:
    print("Error: La clave 'pais' no existe en el diccionario.")
