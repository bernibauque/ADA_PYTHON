# Crear un diccionario con información de una persona
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Barcelona",
    "profesion": "Ingeniero"
}

# Imprimir el diccionario original
print("Diccionario original:", persona)

# Usar .popitem() para eliminar y obtener el último par clave-valor
ultimo_elemento = persona.popitem()

# Imprimir el par clave-valor eliminado
print("Último par clave-valor eliminado:", ultimo_elemento)

# Imprimir el diccionario después de usar .popitem()
print("Diccionario después de usar .popitem():", persona)

# Repetir el uso de .popitem() para ver cómo cambia el diccionario
otro_elemento = persona.popitem()
print("Otro par clave-valor eliminado:", otro_elemento)
print("Diccionario después de otra eliminación:", persona)

