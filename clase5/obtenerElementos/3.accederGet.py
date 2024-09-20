# Crear un diccionario con información de una persona
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Barcelona"
}

# Usar el método .get() para acceder a los elementos
nombre = persona.get("nombre")
edad = persona.get("edad")
ciudad = persona.get("ciudad")

# Imprimir los valores obtenidos
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# Intentar acceder a una clave que no existe usando .get()
# En lugar de lanzar un error, devuelve None
pais = persona.get("pais")
print("País:", pais)  # Esto imprimirá 'País: None'

# Usar .get() con un valor predeterminado si la clave no existe
pais_con_valor_predeterminado = persona.get("pais", "No especificado")
print("País (con valor predeterminado):", pais_con_valor_predeterminado)
