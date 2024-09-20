# Ejemplo 1 - basico de return
def calcular_cuadrado(numero):
    return numero * numero 
resultado = calcular_cuadrado(4)

print("Ejemplo basico de return: ")
print(f"El cuadrado de 4 es {resultado} ")
print()

# Ejemplo 2 - Retorno de multiples valores
def obtener_datos():
    nombre = "Ana"
    edad = 30
    return nombre, edad # Retorne los valores como una tupla
# Asignamos los valores a una variable
nombre, edad = obtener_datos()
print("Ejemplo 2 - Retorno de multiples valores: ")
print(f"Nombre: {nombre}, Edad: {edad}")
print()

# Ejemplo 3 - return con condicional
def clasificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else: 
        return "Cero"
    
resultado1 = clasificar_numero(10)
resultado2 = clasificar_numero(-5)
resultado3 = clasificar_numero(0)

print("Ejemplo 3 - Sin return: ")
print(f"El numero 10 es {resultado1}")
print(f"El numero -5 es {resultado2}")
print(f"El numero 0 es {resultado3}")
print()

# Ejemplo 4: Sin return
def mostrar_mensaje():
    print("Esta funcion no retorna valor.")
resultado = mostrar_mensaje()
print("Ejemplo 4: Sin return")
print(f"Valor retornado {resultado}")


