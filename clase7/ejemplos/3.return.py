# Ejemplo 1: Básico de 'return'
def calcular_cuadrado(numero):
    return numero * numero  # Retorna el cuadrado del número

# Llamada a la función y almacenamiento del resultado
resultado = calcular_cuadrado(4)

# Imprimimos el resultado
print("Ejemplo 1: Básico de 'return'")
print(f"El cuadrado de 4 es {resultado}")
print()

# Ejemplo 2: Retorno de múltiples valores
def obtener_datos():
    nombre = "Ana"
    edad = 30
    return nombre, edad  # Retorna dos valores como una tupla

# Asignamos los valores retornados a variables
nombre, edad = obtener_datos()

# Imprimimos los valores
print("Ejemplo 2: Retorno de múltiples valores")
print(f"Nombre: {nombre}, Edad: {edad}")
print()

# Ejemplo 3: Sin 'return'
def mostrar_mensaje():
    print("Esta función no retorna un valor.")

# Llamamos a la función
resultado = mostrar_mensaje()

# Imprimimos el valor retornado
print("Ejemplo 3: Sin 'return'")
print(f"Valor retornado: {resultado}")  # Output: None
print()

# Ejemplo 4: 'return' con condiciones
def clasificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# Llamadas a la función con diferentes argumentos
resultado1 = clasificar_numero(10)
resultado2 = clasificar_numero(-5)
resultado3 = clasificar_numero(0)

# Imprimimos los resultados
print("Ejemplo 4: 'return' con condiciones")
print(f"El número 10 es {resultado1}")
print(f"El número -5 es {resultado2}")
print(f"El número 0 es {resultado3}")
