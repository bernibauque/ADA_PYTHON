# Crear una tupla con elementos repetidos
mi_tupla = (1, 2, 3, 1, 4, 1, 5)

# Contar cuántas veces aparece el número 1 en la tupla
numero_de_unos = mi_tupla.count(1)

# Mostrar el resultado
print("El número 1 aparece", numero_de_unos, "veces en la tupla.")

# Explicación:
# La tupla (1, 2, 3, 1, 4, 1, 5) contiene el número 1 tres veces.
# El método count(1) cuenta estas apariciones y devuelve 3.

# Contar cuántas veces aparece el número 7 en la tupla
numero_de_siete = mi_tupla.count(7)

# Mostrar el resultado
print("El número 7 aparece", numero_de_siete, "veces en la tupla.")

# Explicación:
# El número 7 no está en la tupla, por lo que el método count(7) devuelve 0.

