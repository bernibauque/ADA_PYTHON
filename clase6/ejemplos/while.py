# Programa para adivinar un número secreto

# Definir el número secreto
numero_secreto = 7

# Inicializar la variable para almacenar el número del usuario
numero_adivinado = None

# Mensaje inicial
print("Adivina el número secreto (entre 1 y 10):")

# Bucle while que continúa hasta que el usuario adivine el número secreto
while numero_adivinado != numero_secreto:
    # Solicitar al usuario que ingrese un número
    numero_adivinado = int(input("Introduce tu número: "))
    
    # Comprobar si el número adivinado es correcto
    if numero_adivinado < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif numero_adivinado > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.")

# Mensaje final cuando el ciclo termina
print("Gracias por jugar.")


