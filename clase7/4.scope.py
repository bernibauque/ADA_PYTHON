# Scope: Alcance local y global en Python

# Variable Global
x = 20

def funcion_local():
    x = 10 # X es una variable local
    print(f"Valor de x dentro de la funcion local: {x}")

def funcion_global():
    #global x #Para modificar la variable global 
    x = 30 
    print(f"Valor de x dentro de la funcion global: {x}")


funcion_local()
funcion_global()

print(f"Valor de x fuera de la funcion: {x}")