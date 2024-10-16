#Este programa es un juego de trivia sobre programacion en python

#Importacion modulo ramdom
import random

def juego_trivia():
    # Pedir el nombre y la edad
    nombre = input("¡Hola! ¿Cómo te llamas? ")
    edad = int(input(f"¡Hola {nombre}! ¿Cuántos años tienes? "))

    # Verificar si cumple con la edad mínima
    if edad < 18:
        print("Lo siento, debes tener al menos 18 años para jugar.")
        return
    
    # Bienvenida y explicación del juego
    print(f"¡Bienvenido/a al juego, {nombre}!")
    print("En este juego de trivia, pondremos a prueba tus conocimientos de python.")
    print("Responderás varias preguntas relacionadas con el tema. ¡Buena suerte!\n")

    # Lista de preguntas y respuestas (usando tuplas)
    preguntas_respuestas = [
        ("¿Cual es la diferencia entre listas y tuplas?", "Las tuplas son inmutables y Las Listas son mutables"),
        ("¿Ques es python?", "Un lenguaje de programación interpretado y de alto nivel"),
        ("¿Quien es el creador de Python?", "Guido Van Rossum"),
        ("¿Que es un lenguaje tipado?", "Exige que se declare el tipo de dato en las variables"),
        ("¿En que año se lanzo la primera versión de python?", "1991"),
        ("¿Que es la terminal", "Un programa con el cual le damos ordenes al sistema"),
        ("¿Cual podria ser un tipo de dato String", "Hola"),
        ("¿Por que se crean lo bucles infinitos?", "Por que la condición nunca llego a ser falsa")
    ]

    # Mezclar las preguntas aleatoriamente
    random.shuffle(preguntas_respuestas)

    # Mostrar preguntas al jugador y contar las respuestas correctas
    respuestas_correctas = mostrar_preguntas(preguntas_respuestas)

    # Finalizar el juego y mostrar el resultado
    fin_juego(respuestas_correctas)

# Función para mostrar las preguntas y contar las respuestas correctas
def mostrar_preguntas(preguntas_respuestas):
    errores_consecutivos = 0
    respuestas_correctas = 0  # Asegurarse de que sea un entero desde el inicio

    # Mostrar cada pregunta al jugador
    for pregunta, respuesta_correcta in preguntas_respuestas:
        respuesta_jugador = input(f"{pregunta}\nTu respuesta: ")

        # Validar la respuesta
        if verificar_respuesta(respuesta_jugador, respuesta_correcta):
            print("¡Correcto!\n")
            respuestas_correctas += 1  # Aquí estamos sumando 1 correctamente
            errores_consecutivos = 0  # Reiniciar el conteo de errores consecutivos
        else:
            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}\n")
            errores_consecutivos += 1

        # Si comete 3 errores consecutivos, termina el juego
        if errores_consecutivos == 3:
            print("Has cometido 3 errores consecutivos. El juego ha terminado.")
            break

    return respuestas_correctas  # Se devuelve el entero respuestas_correctas

# Función para verificar la respuesta del jugador
def verificar_respuesta(respuesta_jugador, respuesta_correcta):
    return respuesta_jugador.lower() == respuesta_correcta.lower()

# Función para finalizar el juego y mostrar el resultado final
def fin_juego(respuestas_correctas):
    print(f"Has respondido correctamente a {respuestas_correctas} preguntas.")  # respuestas_correctas es int
    print("¡Gracias por jugar! ¡Hasta la próxima!")

# Iniciar el juego
juego_trivia()




