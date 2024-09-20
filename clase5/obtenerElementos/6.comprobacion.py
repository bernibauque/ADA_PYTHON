# Crear un diccionario con información de una persona
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Barcelona"
}

# Comprobar si una clave existe en el diccionario antes de acceder a su valor
clave = "edad"

if clave in persona:
    valor = persona[clave]
    print(f"El valor de '{clave}' es: {valor}")
else:
    print(f"La clave '{clave}' no existe en el diccionario.")

# Intentar acceder a una clave que no existe
clave_inexistente = "pais"

if clave_inexistente in persona:
    valor = persona[clave_inexistente]
    print(f"El valor de '{clave_inexistente}' es: {valor}")
else:
    print(f"La clave '{clave_inexistente}' no existe en el diccionario.")

