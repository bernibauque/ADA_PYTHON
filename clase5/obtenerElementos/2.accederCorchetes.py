# Crear un diccionario con información de una persona
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Barcelona"
}

# Acceder a los elementos del diccionario usando corchetes []
nombre = persona["nombre"]
edad = persona["edad"]
ciudad = persona["ciudad"]

# Imprimir los valores obtenidos
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# Intentar acceder a una clave que no existe
# Esto lanzará un KeyError
# Comentamos esta línea para evitar que el código se detenga
# print(persona["pais"])  


