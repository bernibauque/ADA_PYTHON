import random # Importar modulo random

# Juego Trivia Python
# Creado por Koré Figueroa, Ixzayana Hernandez y Clarissa Nieto
# Este juego tiene el propósito de mostrar una serie de preguntas básicas relacionadas con el
# lenguaje de programación Python, las cuales podrán ser respondidas por el usuario,
# obteniendo una puntuación al final del juego.

def juego_trivia(): # Crear una función que almacene la estructura del juego
# Bienvenida del juego, usando print()
    print("===¡BIENVENID@ AL JUEGO DE TRIVIA DE PYTHON!===")
    print("El juego consiste en 10 preguntas de opción múltiple sobre Python, \ntendrás 3 oportunidades para contestar cada pregunta. Después de las 3 oportunidades el juego terminará. \nSi utilizaste más de 2 oportunidades, no se te contará el acierto. \nObtendrás tu puntuación al final del juego. ¡SUERTE!")

# Crear variables nombre y edad, usar un input() para que el usuario pueda agregar su nombre y edad
    nombre = input("Antes de comenzar el juego, ingresa tu nombre por favor: ")
    edad = int(input("Debes de tener mínimo 18 años para jugar, por favor ingresa tu edad: "))  # int para admitir solo números enteros

# Usar un condicional if/else para confirmar que el usuario sea mayor de edad
    if edad >= 18:
        print("Gracias por confirmar tu edad...¡Que comience el juego!")
    else:
        print("Lo sentimos, debes tener mínimo 18 años para jugar, vuelve a intentarlo en un futuro :(")
        exit()  # Terminar el programa si el usuario no cumple con la edad mínima

# Crear las preguntas del juego
# Crear listas vacías para colocar las preguntas y respuestas
# Para manejar mejor los datos, se creó una lista donde cada elemento de la lista es una tupla.
# Dentro de cada tupla se almacenó la pregunta, las opciones de respuesta y la respuesta correcta.
    preguntas = [
    ("¿Cuál de las siguientes opciones es una característica principal de Python?", 
     "A. Tipado No Dinámico / B. Sintaxis Legible / C. No Interactivo / D. Bajo Nivel", 
     "B"),
    ("Son los símbolos utilizados para realizar operaciones sobre variables y valores:", 
     "A. Operadores aritméticos / B. Operadores de asignación / C. Operadores relacionales / D. Operadores lógicos", 
     "A"),
    ("¿Qué número de índice se utiliza para acceder al primer elemento de una lista?", 
     "A. -1 / B. 1 / C. 3 / D. 0", 
     "D"),
    ("Tipo de dato representado por llaves, que contiene pares de claves y valores", 
     "A. Tuplas / B. Listas / C. Diccionarios / D. Conjuntos", 
     "C"),
    ("¿Cuáles son las palabras reservadas empleadas en los ciclos while y for?", 
     "A. Break y Continue / B. def / C. True y False / D. range y len", 
     "A"), 
    ("¿Cual es el comando que se utiliza para concatenar cadenas haciendo interpolacion de variables?", 
     "A. bool[] / B. print(f) / C. if / D. imput()", 
     "B"), 
    ("Palabra clave para devolver un valor al terminar una funcion",
      "A. While / B. def / C. int / D. return", 
      "D"), 
    ("¿Cuantos tipos de parametros existen?",
     "A. 9 / B. 3 / C. 5 / D. 7",
     "B"), 
    ("¿Que es una docstrings?",
     "A. Documento pdf / B. Cadena de texto / C. Comentarios / D. Cadena de caracteres ",
     "B"), 
    ("¿Cual es la manera mas comun para importar un modulo?",
     "A. import random / B. import / C.import shuffle / D. import as rnd",
     "A")
    ]

# Mezclar las preguntas empleando el método shuffle() para asegurar que salgan aleatoriamente
    random.shuffle(preguntas)

    puntuacion = 0  # Inicializar la puntuación
    for pregunta, respuestas, respuesta_correcta in preguntas: # Bucle for para mostrar las preguntas y respuestas
        print("=============================================")  # Para delimitar las preguntas
        print(pregunta)  # Imprimir la pregunta
        print(respuestas)  # Imprimir las opciones de respuesta
        
        intentos = 3  # Número de intentos para responder
        while intentos > 0: # Bucle while para iterar los intentos del usuario, >0 para admitir los intentos
            respuesta_usuario = input("Por favor, ingresa tu respuesta (solo una letra mayúscula): ").upper()  # Agregar input para admitir la respuesta del usuario. Se utilizó .upper() para convertir respuestas en minuscula en mayuscula
            
            if respuesta_usuario == respuesta_correcta: # Condicional if/else para verificar si la respuesta del usuario coincide con la respuesta correcta establecida anteriormente
                print("¡Respuesta correcta! (:")
                puntuacion += 1  # Incrementar la puntuación
                break  # Salir del bucle si la respuesta es correcta
            else:
                intentos -= 1  # Reducir el número de intentos
                puntuacion -=1 # Reducir la puntuación si se equivoca el usario en la pregunta
                if intentos > 0: # Condicional if/else para verificar el número de intentos
                    print(f"Respuesta incorrecta. Te quedan {intentos} intento(s).") # Si aumentan los intentos (es decir, el usuario se equivoca), se mostrará un mensaje que le indique al usuario cuantos intentos le quedan
                else:
                    print(f"Respuesta incorrecta. La respuesta correcta es {respuesta_correcta}.") # Si el usuario se equivoca en los 3 intentos, aparecerá un mensaje indicando cual era la respuesta correcta y ahí terminará el juego
        
        if intentos == 0: # Para indicar que se acabaron los intentos
            print("¡Inténtalo hasta la próxima!")
            exit()  # Terminar el juego si el jugador se queda sin intentos
    
    # Mostrar el puntaje final después de responder todas las preguntas
    print(f"¡Juego terminado! Tu puntuación final es {puntuacion} de {len(preguntas)}. \n¡Gracias por jugar! :)")

# Llamar a la función para iniciar el juego
juego_trivia()



