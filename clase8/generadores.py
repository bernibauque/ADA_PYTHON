# Ejemplo basico de un generador
# Generador que produce numeros del 1 al 5:
# Definicion del generador
def contador():
    # Itera sobre los numeros del 1 al 5
    for i in range(1, 6): #Itera sobre los numeros del 1 al 5 (no contempla el 6)
        yield i #Produce el valor de i y pausa la ejcucion

# crear una instancia para el genrador
gen = contador() # gen es un objeto generador

#Iterar sobre los valores producidos por el generador
for numero in gen:
    print(numero) # Imprime cada numero producido por el generador
    print()
    
#Ejemplo 2 - Fibonacci
def fibonacci():
    a,b = 0,1 #inicializa los primero dos numeros de la secuencia
    while True: #ciclo infinito para generar los numeros
        yield a #produce el valor de a y pausa la ejecucion
        a, b = b, a + b #actualiza a y b para la siguiente iteracion

gen = fibonacci() # gen es un objeto generador que produce numeros de fibonacci

#Obtener los primeros 10 numero de fibonacci
for _ in range(10):
    print(next(gen)) #obtiene el siguiente numero en la secuencia y lo imprime

