import random


def bienvenida():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    
    if edad >= 18:
        print(f"♥️ ¡Bienvenido al juego de Capitales, {nombre}! ♥️")
        print("Ya puedes comenzar a jugar.")
        print("Este juego consiste en responder correctamente las preguntas por medio de opción múltiple.")
        print("¡Comencemos! Mucha suerte ♣️.")
        return nombre, True
    else:
        print("¡Lo sentimos! Debes ser mayor de edad para jugar. Gracias por intentarlo ♥️")
        return nombre, False


def jugar_trivia(nombre):
    preguntas = [
        ("1 - ¿Cuál es la capital de Perú?", ["a- La Paz", "b- Lima", "c- Quito"], "b"),
        ("2 - ¿Cuál es la capital de Francia?", ["a- Berlín", "b- Roma", "c- París"], "c"),
        ("3 - ¿Cuál es la capital de Japón?", ["a- Seúl", "b- Tokio", "c- Beijing"], "b"),
        ("4 - ¿Cuál es la capital de Australia?", ["a- Sídney", "b- Canberra", "c- Melbourne"], "b"),
        ("5 - ¿Cuál es la capital de Canadá?", ["a- Toronto", "b- Ottawa", "c- Vancouver"], "b")
    ]
    
    random.shuffle(preguntas)
    puntaje = 0
    errores_consecutivos = 0  

    for pregunta, opciones, respuesta_correcta in preguntas:
        print(pregunta)
        for opcion in opciones:
            print(opcion)
        
        respuesta = input("Ingrese la opción (a/b/c): ")
        if respuesta == respuesta_correcta:
            print("La respuesta es correcta.\n")
            puntaje += 1
            errores_consecutivos = 0  
        else:
            print("La respuesta es incorrecta.\n")
            errores_consecutivos += 1
        
       
        if errores_consecutivos == 3:
            print("Has respondido incorrectamente tres veces seguidas. El juego ha terminado.\n")
            break
    
    print(f"🎉 ¡Has terminado el juego, {nombre}! 🎉")
    print(f"Obtuviste {puntaje} respuestas correctas de {len(preguntas)}.\n")
    print("¡Gracias por jugar! Esperamos verte pronto en otra trivia. ¡Hasta luego! 😊")


def juego_trivia():
    nombre, es_mayor = bienvenida()
    if es_mayor:
        jugar_trivia(nombre)


juego_trivia()