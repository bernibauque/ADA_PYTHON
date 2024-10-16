# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes: 

#Modulo random (paso 4)
import random 
print('¡Te doy la bienvenida a la Trivia sobre Python!')
# Paso 3
# Nombre usuario
nombre = input('Ingresa tu nombre, por favor: ')
# Edad usuario
edad = int(input('Ingresa tu edad, por favor: '))

if edad >= 18:
    print(f' \n¡Hola {nombre}, Es hora de comenzar con la Trivia sobre python!\n ')
    print('Antes de comenzar, las instrucciones del juego son las siguientes: ')
    print('debes de contestar correctamente las preguntas, por cada respuesta correcta \nvas a ganar 1 punto. Sin emabrgo, por cada respuesta incorrecta \nno sumaras puntos, pero si te equivocas más de tres veces pierdes el juego.')
    print('¡Ahora si, a jugar!')
    print('------------------------------------')
else:
    print(f'Lo siento {nombre}, no tienes la edad mínima para jugar. ')
    exit()

# Paso 5 preguntas y respuestas
# Definir las preguntas y sus respuestas en un diccionario
Preguntas = [
    ('¿Un algoritmo es un conjunto de instrucciones secuenciales que permiten la resolución de un problema?', True), 
    ('Son ejemplos de lenguajes interpretados: Ruby, JavaScript y Python' , True),
    ('En el ámbito de la informática, la identación cumple una función similar a la de la sangría en la escritura formal del lenguaje humano', True),
    ('¿La identación es obligatoria en Python? ', True),
    ('Se encarga de ejecutar una misma acción “mientras que” una determinada condición se cumpla. ¿Lo anterior corresponde al bucle for?', False)] # FALTA AÑADIR LAS PREGUNTAS!

# Usar shuffle para mezclar las preguntas 
random.shuffle(Preguntas)

# Contador de los errores consecutivos
score = 0
errores = 0

# Recorrer cada pregunta
for pregunta, respuesta_correcta in Preguntas: #Ciclo for para que me muestre las preguntas de manera aleatoria
    respuesta_usuario = input(f'{pregunta} (Responde Verdadero o Falso): ').lower()

    if respuesta_usuario == respuesta_correcta:
        print('Es correcto')
        score += 1
    else:
        print('Es incorrecto')
        errores += 1
        if errores >= 3:
            print(f'Tu puntuacion es de {errores}', "\nJuego Terminado")
            break


# Enseñar la pregunta al usuario
    print(f'Pregunta: {pregunta}')
# Imprimimos las preguntas mezcladas

#Obtener la respuesta del usuario
respuesta_usuario = input('Ingresa tu respuesta: ')

# paso 7 aumentar al contador de respuestas correctas
score = int(score / len(Preguntas) * 100)
print(f'Tu puntaje es: {score}%')
