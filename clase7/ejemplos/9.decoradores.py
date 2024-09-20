# Definición del decorador básico
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return wrapper

# Usamos el decorador en una función
@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamamos la función decorada
print("=== Decorador en una función ===")
saludar("Ana")

# Decorador con parámetros
def repetir_veces(veces):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir_veces(3)
def decir_hola():
    print("Hola!")

print("\n=== Decorador con parámetros ===")
decir_hola()


def repetir_veces(veces):          # 1. Definición de un decorador generador que acepta un parámetro 'veces'
    def decorador(func):           # 2. Definición de un decorador dentro del decorador generador
        def wrapper(*args, **kwargs):  # 3. Definición de la función interna 'wrapper' que acepta argumentos
            for _ in range(veces):    # 4. Ejecuta la función original 'veces' veces
                func(*args, **kwargs)   # 5. Llamada a la función original
        return wrapper               # 6. Retorna la función 'wrapper' que reemplaza a la función original
    return decorador                # 7. Retorna el decorador para ser usado con el número de veces especificado

@repetir_veces(3)                  # 8. Aplica el decorador 'repetir_veces' con el argumento 3 a la función 'decir_hola'
def decir_hola():                  # 9. Definición de la función 'decir_hola'
    print("Hola!")                 # 10. Código de la función 'decir_hola'

decir_hola()                       # 11. Llama a la función 'decir_hola'

