import random
def solicitar_nombre_y_edad():
    """Utilizo la función para solicitar nombre y edad del usuario, con input para que el usuario escriba
    su nombre por consola e int + input para que el usuario ingrese un número entero."""
    
    nombre = input("¡Hola, te doy la bienvenida a TRIVIPY! \n¿Cuál es tu nombre? \n ")
    edad = int(input("\n¿Qué edad tenés? \n "))
    return nombre, edad
def verificar_edad(edad):
    """Verificar la edad mínima de 18 años y si se cumple la condición iniciar el juego
    Se utiliza el condicional if para permitirle participar si cumple la condición caso se emite
    un mensaje informando que no puede participar"""
    
    if edad >= 18:
        print("¿Estás preparado/a para jugar? \n\n¡Comienza el desafío, qué te diviertas!\n")
        return True
    else:
        print("Lo siento, la edad mínima para participar es de 18 años. ¡Te espero pronto!")
        return False
def mostrar_bienvenida(nombre):
    """ Si cumple la condición de la mayoría de edad se imprimirá el mensaje de bienvenida y las bases
    para participar del juego"""
    
    print(f"\t¡Bienvenido/a {nombre} a TRIVIPY! Espero que te diviertas.\n\t¿Estás preparado/a para comenzar a jugar?\n")
    print("Las bases del juego son:\nTienes que responder con una sola palabra las preguntas relacionadas con Python.\nPor cada respuesta correcta sumarás 1 punto. Si te equivocas en tres respuestas consecutivas perderás la partida.\n¿Comenzamos?\n¡TRIVIPY TE DESEA MUCHA SUERTE!")
def mezclar_preguntas(preguntas):
    random.shuffle(preguntas)
    return preguntas
def obtener_preguntas():
    """Se utilizan tuplas para organizar las preguntas y respuestas dentro de una lista """
    return [
        ("¿Los operadores en Python son sólo aritméticos?", "NO"),
        ("¿Python es un programa o un lenguaje?", "LENGUAJE"), 
        ("¿Qué clave se utiliza para ejecutar un bloque de código sólo si se cumple una condición específica?", "IF"),
        ("¿Las listas son mutables, dinámicas, ordenadas y pueden anidarse?", "SI"),
        ("¿Qué tipo de dato se utiliza para manejar condiciones y realizar operaciones lógicas?", "BOOL"),
        ("¿Cuál es el método que cuenta la cantidad de veces que aparece un elemento dentro de una tupla?", "COUNT"),
        ("¿Cómo se llama el proceso por el cual se puede obtener una parte determinada de una lista?", "SLICING"),
        ("Se puede decir que es una buena práctica comprobar la existencia de una clave antes de acceder a un diccionario. ¿Esto es correcto?", "SI"),
        ("¿Cuál es el operador que se utiliza para eliminar elementos de un diccionario?", "DEL"),
        ("¿Qué función se utiliza para crear un conjunto?", "SET")
    ]
def verificar_respuesta(pregunta, respuesta_correcta):
    """ Se utiliza la función para verificar si la respuesta es correcta. Deberá buscar si la respuesta
    que responde el jugado es correcta o no y emitirá un mensaje informando el resultado. Si la respuesta
    es incorrecta además mostrará cuál era la verdadera. Retornando a la lista de preguntas para seguir
    jugando."""
    
    print(f"La pregunta es: {pregunta}")
    respuesta_participante = input("Tu respuesta es: ")
    if respuesta_participante.lower() == respuesta_correcta.lower():
        print("¡Muy bien! Sigue respondiendo.")
        return True
    else:
        print(f"Incorrecta. La respuesta correcta es: {respuesta_correcta}")
        return False
def juego_trivia():
    """Función principal para jugar a la trivia: Solicitar el nombre y la edad, verificar si la edad es
    válida para participar, mostrar el mensaje de bienvenida, obtener y mezclar las preguntas e iniciar el juego.
    La partida se termina si el jugador comete tres errores consecutivos o si responde correctamente a 
    todas las preguntas.
    Las variables son:
    nombre (str): Nombre
    edad (int): Edad 
    preguntas (list): Lista de preguntas y respuestas correctas.
    contador_respuestas_correctas (int): Contador de respuestas correctas.
    contador_errores (int): Contador de errores consecutivos.
    """
    
    nombre, edad = solicitar_nombre_y_edad()
    if verificar_edad(edad):
        mostrar_bienvenida(nombre)
        preguntas = mezclar_preguntas(obtener_preguntas())
        contador_respuestas_correctas = 0
        contador_errores = 0
        
        for pregunta, respuesta_correcta in preguntas:
            if verificar_respuesta(pregunta, respuesta_correcta):
                contador_respuestas_correctas += 1
                contador_errores = 0
            else:
                contador_errores += 1
                if contador_errores == 3:
                    print("Has cometido tres errores consecutivos. ¡Fin del juego!")
                    break
        
        if contador_errores < 3:
            print(f"¡Felicitaciones {nombre}! ¡GANASTE! Obtuviste {contador_respuestas_correctas} respuestas correctas.")
            print("¡Gracias por jugar! Te espero en un nuevo desafío.\n ¡HASTA LA PRÓXIMA!")
juego_trivia ()  
