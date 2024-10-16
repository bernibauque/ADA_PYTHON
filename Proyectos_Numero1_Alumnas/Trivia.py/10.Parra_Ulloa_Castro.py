# Este comando pertenece al Paso 4 de la Consigna: importar el módulo random.
import random

# Paso 2: Crear el archivo y escribir un comentario inicial de lo que tratará el Programa.

# Proyecto Número 1: Crea tu Primer Juego de Trivia en Python.
# Curso: Python Intensivo.
# Profesora: Bauque Bernardita.
# Alumnas: Emi Parra, Berenice Castro y María Martha Ulloa.

# Paso 3: Estructura Básica del Juego

# Define el flujo principal del programa: Tu programa comenzará pidiendo al usuario su nombre y edad.
print("¡Hola!. Antes de comenzar por favor ingresa la siguiente información personal:")
input("Nombre: ")
# Aquí guardaré la información en la variable "Edad" para después verificar si es mayor de 18 años.
edad = int(input("Edad: "))

# Verifica si el jugador cumple con la edad mínima para jugar (18 años). Si no cumple, el juego deberá terminar.
edad_minima = 18  # Variable de la edad mínima para jugar

# Lo que haré a continuación es establecer un programa que verifique la edad.
if edad >= edad_minima:
    # Le damos la Bienvenida al usuario si su edad es mayor o igual a 18.
    print("\n¡Bienvenida al juego de Trivia en Python!")
else:
    # Si la edad del usuario es menor a 18 este comando terminan la ejecución del programa.
    exit()

# Configura la bienvenida del juego:
print("Esperamos que aprendas y también te diviertas al responder estas preguntas de Programación.")
print("El juego funcionará de la siguiente manera: te presentaremos una serie de preguntas que retarán tus conocimientos de Programación en Python.")
print("Las preguntas serán de opción múltiple y tu ingresarás el inciso que creas que sea correcto.")
print("Lee detenidamente cada pregunta y tómate tu tiempo para responder.")
print("Al final, podrás verificar cuántas preguntas acertaste.")
print("Te deseamos el mejor de los éxitos.¡Comencemos!")
print("\nLee cada pregunta y responde SOLAMENTE con el NÚMERO del inciso que creas correcto:")

# Paso 5: Crear las preguntas del juego

# Usa una lista para almacenar las preguntas, y asocia cada pregunta con su respuesta correcta.
# Aquí ustedes me dirán chicas. Se me hace más sencillo incluir en la pregunta las opciones de respuesta.
# El jugador deberá ingresar mediante input() el número del inciso correcto.
# El hecho de que la entrada sea un número pienso que nos puede ayudar a simplificar el conteo de respuestas correctas.
# De igual manera modifiquen las preguntas como consideren correcto.

# Organiza las preguntas y respuestas en una estructura de datos:
# Usa tuplas para guardar cada pregunta junto con su respuesta correcta. Coloca estas tuplas dentro de una lista.
preguntas_respuestas = [
    ("¿Qué es Python?\n 1) Un lenguaje de programación. \n 2) Un tipo de serpiente. \n 3) Un tipo de comando.", 1),
    ("¿Qué es una variable en Python?\n 1) Un dato anidado. \n 2) Un espacio que almacena un valor. \n 3) Un diccionario.", 2),
    ("¿Cuál es un dato básico en Python?\n 1)'n\' \n 2) # \n 3) int", 3),
    ("¿Cómo se define una lista en Python?\n 1) () \n 2) [] \n 3) {} ", 2),
    ("¿Cómo se define una lista inmutable en Python?\n 1) () \n 2) [] \n 3) *", 1),
    ("En Python las Tuplas son Mutables.\n 1) Verdadero. \n 2) Falso.", 2),
    ("¿Para qué se utiliza print() en Python?\n 1) Para conectar tu impresora. \n 2) Para hacer una lista. \n 3) Muestra información en la consola.", 3),
    ("¿Cuál es el operador de asignación en Python?\n1) = \n2) + \n3) *", 1)
]

# Mezclar las preguntas para que aparezcan en un orden diferente cada vez que jueguen:
# Usamos esa función para mezclar aleatoriamente los elementos de la lista. Es este caso, el orden de las preguntas.
random.shuffle(preguntas_respuestas)
# print(preguntas_respuestas) # Nos muestra las preguntas y respuestas cada vez en un orden diferente.

# Paso 6: Mostrar las preguntas al jugador.

# ATENCIÓN: En este paso falta "Controlar los intentos fallidos del jugador".

# Contador de respuestas correctas
aciertos = 0
# Contador de errores consecutivos (3 maximo consecutivos o se acaba el juego. Si contesta bien vuelve a 3)
errores_consecutivos = 3

# Usa un bucle for para mostrar cada pregunta al jugador:
for pregunta, respuesta_correcta in preguntas_respuestas:
    if errores_consecutivos == 0:
        print('Te quedaste sin intentos. Vuelve a empezar')
        break  # Si errores consecutivos llega a 0, se deja de ejecutar
    print(pregunta)  # Muestra las preguntas con sus tres posibles respuestas.
    # El jugador debe ingresar el número del inciso que crea que es correcto.
    tu_respuesta = int(input("Tu respuesta es: "))

    # Paso 7: Validar respuestas: Compara la respuesta del jugador con la respuesta correcta.
    if tu_respuesta == respuesta_correcta:
        print("¡Correcto!\n")
        aciertos += 1  # Aumenta en 1 el contador de aciertos.
        errores_consecutivos = 3  # si responde correctamente el contador de errores vuelve a 3
        continue  # si respondes bien continua con la que sigue
    else:
        # Si la respuesta es incorrecta te muestra el resultado correcto.
        # Y le resta un intento de los 3 consecutivos que tiene el usuario
        errores_consecutivos -= 1
        print(f"Incorrecto. El inciso correcto es el: {
              respuesta_correcta}. Te queda {errores_consecutivos} intentos\n")


# Paso 8: Crear Funciones.

# Función de bienvenida que solicita el nombre y la edad del usuario


def bienvenida():
    print("¡Hola!\n Antes de comenzar por favor ingresa la siguiente información personal:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    return nombre, edad

# Función para validar la edad del usuario


def validar_edad(edad):
    edad_minima = 18
    if edad >= edad_minima:
        print("\n \x1b[1m¡Bienvenida al juego de Trivia en Python!\x1b[0m")
        print("Esperamos que aprendas y también te diviertas al responder estas preguntas de Programación.")
        print("El juego funcionará de la siguiente manera: te presentaremos una serie de preguntas que retarán tus conocimientos de Programación en Python.")
        print("Las preguntas serán de opción múltiple y tu ingresarás el inciso que creas que sea correcto.")
        print("\nLee detenidamente cada pregunta y tómate tu tiempo para responder.")
        print("Al final, podrás verificar cuántas preguntas acertaste.")
        print("Te deseamos el mejor de los éxitos.\n¡Comencemos!")
        print(
            "\n \x1b[1mLee cada pregunta y responde SOLAMENTE con el NÚMERO del inciso que creas correcto:\x1b[0m \n")
        return True
    else:
        print(
            "No cumples con la edad mínima para participar en este juego.\n Lo siento :c ")
        return False

# Función que selecciona las preguntas y verifica las respuestas


def juego_trivia(preguntas_respuestas):
    aciertos = 0
    errores_consecutivos = 3

    for pregunta, respuesta_correcta in preguntas_respuestas:
        if errores_consecutivos == 0:
            print('Te quedaste sin intentos. Vuelve a empezar')
            break
        print(pregunta)
        tu_respuesta = int(input("\nTu respuesta es: "))

        if tu_respuesta == respuesta_correcta:
            print("¡Correcto!\n")
            aciertos += 1
            errores_consecutivos = 3
        else:
            errores_consecutivos -= 1
            print(f"Incorrecto. El inciso correcto es el: {
                  respuesta_correcta}. Te queda {errores_consecutivos} intentos\n")

    return aciertos


# Punto 9:
# Al finalizar el juego, muestra cuántas respuestas correctas obtuvo el jugador.
# Utiliza print() para mostrar el puntaje final del jugador.
# Agradece al jugador por participar y despide el juego de manera amigable.`

nombre, edad = bienvenida()
if validar_edad(edad):
    random.shuffle(preguntas_respuestas)  # Mezcla las preguntas aleatoriamente
    puntaje = juego_trivia(preguntas_respuestas)
    print(f"\n{nombre}, obtuviste {puntaje} puntos de {
          len(preguntas_respuestas)} posibles.")
    print("\x1b[1m¡Muchas gracias por haber participado en este juego, esperamos verte de nuevo!\x1b[0m")