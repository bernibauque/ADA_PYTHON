# Definición de la función con un parámetro
def calcular_doble(numero):
    doble = numero * 2  # Calcula el doble del argumento
    print(f"El doble de {numero} es {doble}")

# Llamadas a la función con diferentes argumentos
calcular_doble(5)   # Output: El doble de 5 es 10
calcular_doble(12)  # Output: El doble de 12 es 24
calcular_doble(7)   # Output: El doble de 7 es 14

# Definición de una función que utiliza parámetros posicionales, con nombre y predeterminados
def presentar_persona(nombre, edad, ciudad="Desconocida", profesion="Desconocida"):
    """
    Presenta información sobre una persona.

    Parámetros:
    - nombre: (str) Nombre de la persona.
    - edad: (int) Edad de la persona.
    - ciudad: (str) Ciudad donde vive la persona (opcional).
    - profesion: (str) Profesión de la persona (opcional).
    """
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesión: {profesion}")
    print()  # Línea en blanco para separar la salida de diferentes llamadas a la función

# Ejemplos de llamadas a la función

# Usando argumentos posicionales
print("Ejemplo con argumentos posicionales:")
presentar_persona("Ana", 30)  # 'ciudad' y 'profesion' usarán el valor predeterminado

# Usando argumentos posicionales y con nombre
print("Ejemplo con argumentos posicionales y con nombre:")
presentar_persona("Luis", 25, ciudad="Madrid", profesion="Ingeniero")  
# 'nombre' y 'edad' son posicionales, 'ciudad' y 'profesion' son con nombre

# Usando todos los argumentos con nombre
print("Ejemplo con todos los argumentos con nombre:")
presentar_persona(nombre="Marta", edad=28, ciudad="Barcelona", profesion="Diseñadora")  
# Todos los argumentos son con nombre

# Usando argumentos posicionales y un argumento con nombre
print("Ejemplo con argumentos posicionales y un argumento con nombre:")
presentar_persona("Carlos", 35, profesion="Profesor")  
# 'nombre' y 'edad' son posicionales, 'profesion' es con nombre, 'ciudad' usa el valor predeterminado
