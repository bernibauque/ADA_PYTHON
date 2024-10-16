# Este es un juego de Trivia de programación en Python.

# Módulo random
import random

# Estructura básica del juego

# Bienvenida + explicación del juego
bienvenida = "¡Bienvenido/a a la Trivia Python! Un juego donde descubrirás qué tanto sabes del lenguaje de programación Python."
print(bienvenida)

explicacion_deljuego = """Estamos muy felices de probar tus conocimientos en programación Python. 
Jugaremos de la siguiente manera: durante el juego estaremos lanzando preguntas y tú deberás responder con la respuesta correcta. 
Cada respuesta correcta te dará un punto. Si respondes incorrectamente 3 veces, el juego terminará. 
Veamos cuántos puntos consigues, ¡Comencemos con la trivia!\n"""

# Definir datos del jugador
def datosdeljugador():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    
    if edad < 18:
        print("¡Ups!, no tienes la edad suficiente para jugar. Prueba en unos años más.")
        exit()  # Si tiene menos de 18, se acaba el juego.
    else:
        print(f"¡Juguemos, {nombre}!") # Si tiene más de 18, jugamos.
        print(explicacion_deljuego) # Y ahora explicamos de qué va el juego.
    
    return nombre # Para que nos devuelva el nombre para usarlo al rato.

def mezclar_preguntas(preguntas_y_respuestas): #Con esto mezclamos las preguntas.
    random.shuffle(preguntas_y_respuestas)

# Lista de preguntas y respuestas
preguntas_y_respuestas = [
    ("¿Cómo se llama una secuencia de pasos finitos para resolver un problema?", "Algoritmo"),
    ("¿Qué tipo de dato representa números decimales en Python?", "Float"),
    ("¿Qué símbolo se usa para hacer un comentario de una sola línea en Python?", "#"),
    ("¿Cómo se llama el tipo de dato que puede ser True o False?", "Boolean"),
    ("¿Cuál es el operador aritmético para la división en Python?", "/"),
    ("¿Qué palabra clave usas para ejecutar código si una condición es verdadera?", "if"),
    ("¿Qué estructura de datos se usa para almacenar múltiples elementos en orden en Python?", "Lista"),
    ("¿Qué método de las tuplas cuenta la aparición de un elemento?", "count"),
    ("¿Cómo se llama la estructura de datos en Python que almacena pares clave-valor?", "Diccionario"),
    ("¿Cuál es el resultado de not True en una tabla de verdad?", "False")
]

mezclar_preguntas(preguntas_y_respuestas) # Aquí llamando a la función mezcladora

def juego_trivia(): # Definimos la dinámica de la trivia
    
    nombre = datosdeljugador() #Pedimos los datos del jugador
    
    # Así contamos los errores y aciertos
    errores = 0
    aciertos = 0

    # Bucle para mostrar cada pregunta
    for pregunta, respuesta_correcta in preguntas_y_respuestas:
        # Solicitar la respuesta al jugador
        respuesta_usuario = input(f"{pregunta} ")

        # Comparamos la respuesta del usuario con la respuesta correcta
        if respuesta_usuario.strip().lower() == respuesta_correcta.lower():  # Uso de strip para eliminar espacios y lower para ignorar mayúsculas y minúsculas
            print("¡Respuesta Correcta!")
            aciertos += 1  # Contamos aciertos
        else:
            print("Lo siento, es una respuesta incorrecta.")
            errores += 1  # Contadomos errores
        
        # Si el número de errores llega a su máximo
        if errores == 3:
            print("¡Uy! Acumulaste el máximo de errores. El juego ha terminado :(")
            break  # Termina el juego

    # Mensajes finales según los aciertos
    if aciertos == 8:
        print("¡Genial!, tu puntuación es de 8. Sigue prepárandote. Gracias por jugar a la Trivia Python.")
    elif aciertos == 9:
        print("¡Wow! tu puntuación es de 9. Muy bien jugado. Gracias por jugar a la Trivia Python.")
    elif aciertos == 10:
        print("¡OMG! ¡Tu puntuación está de 10 como tu conocimiento en Python. ¡Felicidades! Gracias por jugar a la Trivia Python.")
    else:
        print(f"Conseguiste {aciertos} aciertos, {nombre}. ¡Recuerda que la práctica es lo más importante! Gracias por jugar a la Trivia Python.")

# Llamamos a la función para comenzar el juego ♥
juego_trivia()