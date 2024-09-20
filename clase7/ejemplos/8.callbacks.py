# Ejemplo 1: Callback en una operación básica
# Definimos las funciones de callback
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# Función que recibe otra función como callback
def operar(a, b, funcion_callback):
    resultado = funcion_callback(a, b)
    print(f"Resultado de la operación: {resultado}")

# Uso de la función operar con diferentes callbacks
print("=== Ejemplo de Callback Simple ===")
operar(5, 3, sumar)  # Resultado de la operación: 8
operar(5, 3, restar)  # Resultado de la operación: 2

# Uso de una lambda como callback
operar(5, 3, lambda a, b: a * b)  # Resultado de la operación: 15
operar(5, 3, lambda a, b: a / b)  # Resultado de la operación: 1.666...

