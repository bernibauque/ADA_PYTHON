# Ejemplo 1 - Callback operacion basica
def suma(a, b):
    return a + b

def restar(a, b):
    return a - b

#Funcion que recibe otra funcion como callback
def operar(a, b, funcion_callback):
    resultado = funcion_callback(a, b)
    print(f"Resultado de la operacion: {resultado}")

# Uso de la funcion operar con diferentes callbacks
print("=== Ejemplo de Callback Simple ===")
operar(5, 3, suma)
operar(5, 3, restar)

#Uso de una lambda como callback
operar(5, 3, lambda a, b: a * b)
operar(5, 3, lambda a, b: a / b)

