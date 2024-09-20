# Ejercicio 5: Manejo de Matrículas en una Tupla
# Consigna:

# Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
# Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
# Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.

# Crear la tupla
matriculas = (101, 102, 103, 104, 105)

# Contar cuántas veces aparece el número 102
conteo_102 = matriculas.count(102)
print("El número de matrícula 102 aparece", conteo_102, "veces en la tupla.")

# Encontrar la posición del número 104
indice_104 = matriculas.index(104)
print("El número de matrícula 104 se encuentra en la posición", indice_104, "de la tupla.")
