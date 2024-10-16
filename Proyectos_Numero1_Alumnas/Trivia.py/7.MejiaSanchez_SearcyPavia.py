#Mejía Sánchez, Pamela
#Searcy Pavia, Ivone



#Este es un juego de trivia que consiste en 10 preguntas aleatorias con opcion multiple  
#La temática que se aborda en las preguntas es sobre programacion con python

import random # Importamos el modulo random por que realizaremos preguntas aleatorias.

#Definimos las preguntas y respuestas primero en una lista, después en un diccionario y creamos 
# las tuplas para cada pregunta y que no se puedan cambiar. Asimismo, indicar la respuesta correcta
# para que más adelante se pueda llamar a través de una función y se pueda ubicar y valorar los resultados.
preguntas = [
    {
        'pregunta': '¿Qué palabra clave se usa para definir una función en Python?', #pregunta 1
        'opciones': 
        ('a) def', 'b) function', 'c) func'),
        'respuesta_correcta': 'a'
    },
    {
        'pregunta': '¿Cómo se llama el tipo de datos que almacena una secuencia de caracteres?', #pregunta 2
        'opciones': 
        ('a) list', 'b) tupla', 'c) str'),
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': '¿Qué operador se usa para la comparación de igualdad en Python?', #pregunta 3 
        'opciones': 
        ('a) =', 'b) ==', 'c) ==='),
        'respuesta_correcta': 'b'
    },
    {
        'pregunta': '¿Cómo se importa un módulo en Python?', #pregunta 4
        'opciones': 
        ('a) include', 'b) require', 'c) import'),
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': '¿ Cuáles son los tipos de datos en Python?', #pregunta 5
        'opciones': 
        ('a) dinamicas, reasignacion', 'b) numericos, booleanos y cadena de caracteres', 'c) letras y numeros'),
        'respuesta_correcta': 'b'
    },
    {
        'pregunta': 'Es una tecnica que se utiliza en python para unir dos o mas cadenas de texto en una sola a traves del operador +', #pregunta 6
        'opciones': 
        ('a) cadenas de texto', 'b) concatenar cadenas', 'c) suma de variables'),
        'respuesta_correcta': 'b'
    },
    {
        'pregunta': '¿ A que tipo de lenguaje de programacion, segun paradigma, responde python?', #pregunta 7
        'opciones': 
        ('a) Paradigma estructurado', 'b) paradigma orientado a objetos', 'c) Multiparadigma'),
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': 'Describe la sintaxis de la condicional if (if condition)', #pregunta 8
        'opciones': 
        ('a) La condicion la expresas como deseas', 'b) La condicion es la expresión que se evalua y debe ser booleana', 'c) La condicion siempre debe ser verdadera para que se ejecute correctamente', 'd) define'),
        'respuesta_correcta': 'a'
    },
    {
        'pregunta': 'En la lista[a,b,c,d] ¿Cuáles son los indices positivos y negativos que corresponden a c?', #pregunta 9
        'opciones': 
        ('a) positivo = 3, negativo =-2', 'b) positivo = 2, negativo= -2', 'c) positivo =2, negativo=-1'),
        'respuesta_correcta': 'b'
    },
    {
        'pregunta': 'En Python, utilizamos el proceso slicing para obtener una lista a partir de otra, es decir:', #pregunta 10
        'opciones': 
        ('a) una segunda lista', 'b) una lista nueva', 'c) una sublista'),
        'respuesta_correcta': 'c'
    }
]

def bienvenida(): # Definimos funcion bienvenida para recibir al jugador en nuestro juego de trivia con un mensaje e indicaciones
    print('¡Bienvenid@ al juego de trivias sobre Python!')
    print ('Solo tienes 3 oportunidades, después de eso el juego finalizará. ¡Buena Suerte! ')
    bienvenida=print('¿Estas list@?')

def triviatime(): #definimos la funcion triviatime para poder agregar puntuación, de acuerdo a las respuestas del participante.
    puntuacion = 0 
    error=0 
    total = len(preguntas) #Indica el total de preguntas que tenemos (que son 10)

    for pregunta in preguntas: #Realizamos un bucle para poder realizar las preguntas de manera continua.
        muestra_pregunta(pregunta) # Indicamos que se muestre una pregunta del bloque de preguntas.
        respuesta = obtener_respuesta() #Definimos la variable respuesta para que el participante escriba su respuesta.
        if respuesta == pregunta['respuesta_correcta']:  # Planteamos la condicion para la respuesta correcta
            print('¡Correcto!')   #Si es correcto se imprime correcto
            puntuacion = puntuacion + 1 #Si suma un punto a la variable puntuacion de la funcion triviatime 
        else:
            print('Incorrecto') #se imprime la palabra incorrecto en caso de ser respuesta equivocada.
            error=error+1  #Sumamos un punto a la variable error de la funcion triviatime
            if error == 3: #Si se obtienen 3 errores seguidos el juego finaliza
                break  #Esto romple el bucle en caso de tener 3 errores
    print(f'\nTu puntuación final es {puntuacion} de {total}.') #imprimimos el resultado final de la trivia con el total de aciertos sobre 10 preguntas.

def muestra_pregunta(pregunta): #definimos la función para que el programa arroje las preguntas. 
    print(pregunta['pregunta']) #se imprime una pregunta de la lista de preguntas mostrada al inicio del programa
    for opcion in pregunta['opciones']: #Indicamos que opciones debe mostrar de la lista de diccionarios
        print(opcion)  #se muestran las opciones de respuesta en la pregunta.

def obtener_respuesta(): # Definimos la funcion para obtener la respuesta del participante
    respuesta = input('Tu respuesta (a, b, c): ') #Solicitamos al participante que introduzca la respuesta
    return respuesta.strip().lower() #solicitamos que nos devuelva la respuesta y para evitar problemas con 
                                    # los espacios y evitar malentendidos con las mayúsculas se ponen .strip() y .lower()

#Hace que las preguntas se muestren aleatoriamente durante la trivia
random.shuffle(preguntas)

 # Antes de dar la bienvenida, solicitamos el nombre y edad para saber si el participante es mayor de edad.
nombre= (input('Primero necesitamos tu Nombre:')).capitalize()
edad=int(input('Ahora necesitamos tu Edad:')) 
if edad < 18: #Si es menor de 18 no se le permite jugar
    print(f'Lo siento, {nombre}, solo podrás jugar hasta que tengas 18 :(, ¡Cuídate!') 
else: #si es mayor de edad entonces 
    bienvenida() #inicia la funcion bienvenida
    triviatime() #inicia el juego con la función de triviatime que se escribió anteriormente
