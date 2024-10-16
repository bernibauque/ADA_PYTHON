# Este programa es un juego de trivia de capitales de algunos paises en el mundo
# las 2 integrantes de este equipo somos:
# Marcela Kristel Ensaldo Renteria y
# Elsie Vanessa Ensaldo Renteria

# Para importar el módulo random
import random

# Definimos la función principal para correr el juego
def juego_trivia():
    # Solicitamos al jugador su nombre y edad
    nombre = input("¡Bienvenido al juego de trivia! Por favor, ingresa tu nombre: ")
    edad = int(input("Muchas gracias, ahora por favor, ingresa tu edad: "))

    # Verificamos si cumple con la edad mínima para jugar
    if edad < 18:
        print("Lo siento, debes tener al menos 18 años para jugar.")
        return
    
    # Mensajes para el jugador de bienvenida
    print(f"Hola {nombre}, ¡bienvenido a esta entretenida trivia de capitales de paises!")
    print("A continuación, responderás algunas preguntas relacionadas con las capitales de algunos paises.")
    print("Por cada respuesta correcta, ganarás 1 puntos. Si te equivocas 3 veces seguidas, el juego terminará.")
    print("¡Buena suerte! ¡Iniciemos!\n")

    # Preguntas y respuestas
    preguntas = [
        ("¿Cual es la capital de Japon?", "Tokio"),
        ("¿Cuál es la capital de Canadá?", "Ottawa"),
        ("¿Cuál es la capital de Australia", "Canberra"),
        ("¿Cuál es la capital de Brasil", "Brasilia"),
        ("¿Cuál es la capital de Sudafrica?", "Pretoria")
    ]

    # Mezclar las preguntas
    random.shuffle(preguntas)

    # Variables para controlar el juego
    intentos_fallidos = 0
    respuestas_correctas = 0

    # Mostrar preguntas al jugador
    for pregunta, respuesta_correcta in preguntas:
        print(pregunta)
        respuesta_jugador = input("Tu respuesta: ")

        # Validar la respuesta
        if respuesta_jugador.lower() == respuesta_correcta.lower():
            print("¡Correcto!\n")
            respuestas_correctas += 1
            intentos_fallidos = 0  # Reinicia los intentos fallidos si acierta
        else:
            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}\n")
            intentos_fallidos += 1

        # Controlar los intentos fallidos consecutivos
        if intentos_fallidos == 3:
            print("Has cometido 3 errores consecutivos. El juego ha terminado.")
            break

    # Final del juego
    print(f"\nJuego terminado. Respuestas correctas: {respuestas_correctas}")
    print(f"Gracias por jugar, {nombre}. ¡Te esperamos de nuevo pronto!")

# Llamada a la función principal del juego
if __name__ == "__main__":
    juego_trivia()