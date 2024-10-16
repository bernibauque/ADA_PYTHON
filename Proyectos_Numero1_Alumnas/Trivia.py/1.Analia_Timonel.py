
#condicional para verificar si el usuario es mayor de edad
import time
def Tiempo():

    print("***BIENVENIDO A TRIVIA PYTHON***") 
time.sleep(2)

print()
Tiempo()

def usuario():
    
    nombre=input("Por favor ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    
    
    if edad >=18:
        print(" ")
        
        #bienvenida e instrucciones de juego
        def bienvenida(nombre):
                    print(f"""Hola {nombre}, te damos la bienvenida a este juego de trivia que
                    pondra tus conocimientos sobre Python a prueba.
                    El juego consiste en responder la mayor cantidad de preguntas correctas,
                    teniendo solo la oportunidad de fallar 3 veces! 
          
          
                          ¡¡¡¡ MUCHA SUERTE Y A JUGAAAAR =) !!!!""")
        bienvenida(nombre)
#lista de preguntas y respuesta y su vinculacion entre ambas
        def preguntas_juego():
              import random
              preguntas= ["¿Que es un algoritmo? RESPUESTAS:A- es un conjunto ordenado de instrucciones para solucionar un problema.B: es una funcion que permite iterar valores",
              "¿Cual es la palabra reservada para crear una funcion? RESPUESTAS:A- int . B- def",
              "¿ Cual es la funcion del BREAK dentro de un bucle while? RESPUESTAS:A-permite saltear iteraciones que cumplan con un condicional.B-el Break corta la ejecucion una vez se cumpla una condicion",
              "¿Que es una funcion LAMBDA?RESPUESTAS:A-es una funcion anonima, en una sola linea. B- es una funcion que cuenta los valores de una cadena",
              "¿Para que sirven los PARAMETROS y ARGUMENTOS?RESPUESTAS:A- sirven para verificar si un valor esta dentro de una lista o diccionario. B-para pasar datos que utilizaremos en las funciones",
              "¿Que funcion cumple la funcion RANGE?RESPUESTAS: A- se utiliza para generar una secuencia de números enteros.B- se utiliza para organizar los datos de forma ascendente",
              "¿Que hace la funcion LEN? RESPUESTA A: devuelve el numero de valores de un elemento iterable. B- nos marca en que indice se encuentra un valor"]
              respuestas= ["a","b","b","a","b","a","a"]
              preguntas_respuestas=(preguntas[0],respuestas[0]),(preguntas[1],respuestas[1]),(preguntas[2],respuestas[2]),(preguntas[3],respuestas[3]),(preguntas[4],respuestas[4]),(preguntas[5],respuestas[5]),(preguntas[6],respuestas[6])
              random.shuffle(preguntas)
              #contador de vidas y puntos
              puntos=0
              vidas=3
            #bucle para repetir las preguntas mientras vida no sea 3
              while vidas!= 0:
                   #generador de preguntas 
               for p,r in preguntas_respuestas:
                  print("                                                                                    ")
                  print("* Pregunta:", p)
                  print("                                                                                    ")
                   #ingreso de respuesta por parte del usuario
                  respuesta_usuario=input("Ingrese su repuesta: ")
                  respuesta_usuario.lower()
              #verificar si la respuesta del usuario es correcta o incorrecta
                  if respuesta_usuario== r:
                     puntos+=1
                     
                     print("Su repuesta en correcta!!!")
                     print("                                    ")
                     print(f"Puntos:{puntos}")
                  else:
                   print("                                    ")
                   print("Respuesta incorrecta, la respuesta correcta es", r)
                   vidas-=1
                   
                   print("                                    ")
                   print(f"Tenes {vidas} vidas =( ")
                   #mensaje final cuando pierde el juego
                  if vidas==0:
                       print(f"{nombre} tu puntaje final es : {puntos}")
                       print("Hasta la proxima")
                       break
                   
                 
           
                 
                      
             
              
        preguntas_juego()
  
        #condicional en caso de que sea menos de edad
    else:
         print(f"{nombre} no cumple con el requisito de edad minima, hasta pronto!")
        
        
    
usuario()









#temporizador para cerrar la ejecucion
import time
def Tiempo():

    print(" ")
time.sleep(5)

print("ADIOS!")
Tiempo()