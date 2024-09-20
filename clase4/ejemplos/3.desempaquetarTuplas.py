# Ejemplo 1: Desempaquetado Básico de Tuplas
# Crear una tupla con varios tipos de datos
mi_tupla = (1, "Python", 3.14)
# Desempaquetar la tupla en tres variables
numero, lenguaje, pi = mi_tupla
# Mostrar el valor de cada variable después del desempaquetado
print("Número:", numero)       # Imprime: Número: 1
print("Lenguaje:", lenguaje)   # Imprime: Lenguaje: Python
print("Valor de Pi:", pi)      # Imprime: Valor de Pi: 3.14
# Explicación: Aquí, cada valor en la tupla se asigna a una variable correspondiente
# El primer valor de la tupla (1) se asigna a 'numero'
# El segundo valor ("Python") se asigna a 'lenguaje'
# El tercer valor (3.14) se asigna a 'pi'


# Ejemplo 2: Número de Variables no Coincide con el Número de Elementos
# Crear una tupla con tres elementos
mi_tupla = (1, "Python", 3.14)
# Intentar desempaquetar en dos variables (esto causará un error)
# numero, lenguaje = mi_tupla  # Esto causará un ValueError: too many values to unpack (expected 2)
# Explicación: Como hay tres elementos en la tupla y solo dos variables, Python generará un error.
# La cantidad de variables debe coincidir con la cantidad de elementos en la tupla.


# Ejemplo 3: Desempaquetado con el Operador *
# Crear una tupla con varios elementos
mi_tupla = (1, "Python", 3.14, "Tuplas", "Desempaquetado")
# Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto = mi_tupla
# Mostrar los resultados del desempaquetado
print("\nPrimer elemento:", primer_elemento)  # Imprime: Primer elemento: 1
print("Resto de los elementos:", resto)    
# Imprime: Resto de los elementos: ['Python', 3.14, 'Tuplas', 'Desempaquetado']
# Explicación: Aquí, el primer valor de la tupla (1) se asigna a 'primer_elemento'
# El resto de los valores se capturan en la lista 'resto' utilizando el operador '*'
# Esto permite manejar un número variable de elementos en la tupla.

