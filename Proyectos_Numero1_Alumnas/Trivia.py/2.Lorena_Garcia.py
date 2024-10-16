#Este programa es un juego de trivia sobre programación en Python
import random
print("Bienvenido al juego de trivia, en este juego recibiras 5 preguntas aleatorias a las cuales deberas responder usando las opciones (letras) disponibles")
print("¿Cual es tu nombre?")
x = str(input())
print(f"¡Hola {x}! ¡A jugar!")
print("¿Cual es tu edad?")
edad = input()
print("^^^^^^^^^^^^^^^^^^^^^^^^^INICIAMOS^^^^^^^^^^^^^^^^^^^^^^^^^")
print("ノಠ益ಠ)ノ ¡MAY THE ODDS BE EVER IN YOUR FAVOR!")
edad = int(edad)


banco_de_preguntas =[ 
{'Pregunta': 'Es un tipo de dato que no permite cambiar su valor', 'Respuesta': 'A'},
{'Pregunta': 'Cual de los siguientes NO es un lenguaje de programacion?','Respuesta': 'A'}, 
{ 'Pregunta': 'Es una funcion que termina un programa de manera forzosa','Respuesta': 'D'}, 
{'Pregunta': 'Es la instruccion que nos permite mostrar algo en pantalla:','Respuesta': 'A'}, 
{'Pregunta': 'Con esta funcion podemos mostrar numeros aleatorios:','Respuesta': 'B'}
]
opciones_respuestas = [["A.Constante", "B.Variable", "C.Dato", "D.Función"],
["A.HTML", "B.Python", "C.C++", "D.Java"],
["A.range()", "B.input()", "C.len()", "D.break"],
["A.print()", "B.string()", "C.find()", "D.insert()"], 
["A.pop()", "B.random()", "C.index()", "D.get()"]]
puntaje = 0
def checar_resp(resp_jugador, respuesta_correcta):
    if resp_jugador == respuesta_correcta:
        return True
    else:
        return False

i = 1
puntaje = 0
malas = 0

if edad > 17:
    while i < 6:
        vuelta = random.randint(0,4)
        print("============================================================================")
        print(banco_de_preguntas[vuelta]['Pregunta'])
        print(opciones_respuestas[vuelta])
        intento = input("Elige entre las opciones A, B, C, D").upper()
        es_correcto = checar_resp(intento, banco_de_preguntas[vuelta]['Respuesta'])
        i+=1
        if es_correcto:
            print("Correcto!")
            print(f"La respuesta correcta es {banco_de_preguntas[vuelta]['Respuesta']}")           
            puntaje+=1
        else:
            print("Incorrecto :(")
            print(f"La respuesta correcta es {banco_de_preguntas[vuelta]['Respuesta']}")
            malas +=1
            if malas == 3:
                break             

    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")        
    print("¡Gracias por participar!")
    print(f"Tus preguntas correctas van en :{puntaje}")
    print (f"Tus preguntas incorrectas van en :{malas}")
    print(f"Tu puntaje final es {(puntaje/5)*100}%")
    
else:
    print(f"Tu edad es {edad} y eres menor de 18 por lo que no puedes jugar")