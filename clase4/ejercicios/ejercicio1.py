# Ejercicio 1: Operaciones Básicas con Tuplas
# Consigna:

# Crea una tupla llamada mi_tupla con los siguientes elementos: (5, 10, 15, 20, 25).
# Usa el método count para contar cuántas veces aparece el número 10 en la tupla.
# Usa el método index para encontrar la posición del número 20 en la tupla.
# Muestra los resultados de las operaciones anteriores.

# Crear la tupla
mi_tupla = (5, 10, 15, 20, 25)

# Contar cuántas veces aparece el número 10
conteo_10 = mi_tupla.count(10)
print("El número 10 aparece", conteo_10, "veces en la tupla.")

# Encontrar la posición del número 20
indice_20 = mi_tupla.index(20)
print("El número 20 se encuentra en la posición", indice_20, "de la tupla.")
