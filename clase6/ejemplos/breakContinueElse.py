# Programa que pide números hasta que se ingrese un número negativo

# Inicializamos la variable suma para acumular la suma de los 
# números positivos ingresados
suma = 0

# Iniciamos un ciclo infinito usando while True
while True:
    # Solicitamos al usuario que introduzca un número. 
    # La entrada se convierte a entero.
    entrada = int(input("Introduce un número (negativo para terminar): "))
    
    # Verificamos si el número ingresado es negativo
    if entrada < 0:
        # Si el número es negativo, salimos del ciclo usando break
        break  # Salir del ciclo si el número es negativo
    
    # Sumamos el número positivo ingresado a la variable suma
    suma += entrada
    
    # Verificamos si el número ingresado es par
    if entrada % 2 == 0:
        # Si el número es par, usamos continue para saltar la impresión
        # y pasar a la siguiente iteración del ciclo
        continue  # Saltar la impresión para números pares
    
    # Si el número ingresado no es par (es impar), se ejecuta esta línea
    print(f"Número impar ingresado: {entrada}")

# El bloque else se ejecuta cuando el ciclo termina de manera normal,
# sin que se ejecute un break
else:
    print("El ciclo ha terminado porque se ingresó un número negativo.")

# Finalmente, imprimimos la suma de todos los números positivos ingresados
print(f"La suma de los números ingresados es: {suma}")




