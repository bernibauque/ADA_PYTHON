# Alcance Global y Local en Python

# Variable global
x = 20

def funcion_local():
    x = 10  # 'x' es una variable local
    print(f"Valor de x dentro de la función local: {x}")

def funcion_global():
    # Para modificar una variable global, se usa la palabra clave 'global'
    global x
    x = 30
    print(f"Valor de x dentro de la función global: {x}")

# Llamada a las funciones
funcion_local()  # Muestra el valor de x dentro de la función local
# print(x)  
# Esto causará un error porque x está definido en el alcance local de funcion_local()

funcion_global()  # Modifica el valor de x en el alcance global
print(f"Valor de x fuera de la función: {x}")  
# Muestra el valor de x después de modificarlo en la función global


