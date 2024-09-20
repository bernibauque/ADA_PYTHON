# Crear un diccionario con información de una persona
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Barcelona"
}

# Usar el método .items() para obtener todos los pares clave-valor
pares_clave_valor = persona.items()

# Imprimir los pares clave-valor obtenidos
print("Pares clave-valor del diccionario:")
for clave, valor in pares_clave_valor:
    print(f"{clave}: {valor}")

# Convertir los pares clave-valor a una lista de tuplas
pares_lista = list(pares_clave_valor)
print("Pares clave-valor como lista de tuplas:", pares_lista)
