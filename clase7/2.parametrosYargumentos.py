# Definimos una funcion: parametros posisionales, con nombre y predeterminados
def presentar_persona(nombre, edad, ciudad="Desconocida", profesion="Desconocida"):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesion: {profesion}")
    print()

# Ejemplos de llamadas a la funcion

# Usando argumentos posicionales
print("Ejemplo con argumentos posicionales: ")
presentar_persona("Ana", 30)

# Usando argumentos posicionales y con nombre
print("Ejemplo con argumentos posicionales y con nombre: ")
presentar_persona("Luis", 25, ciudad="Madrid", profesion="Ingeniero")

# Usando todos los argumentos con nombre
print("Ejemplo de todos los con argumentos con nombre ")
presentar_persona(nombre="Marta", edad=34, ciudad="Madrid", profesion="Ingeniera")




