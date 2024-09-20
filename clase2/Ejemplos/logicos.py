# Definimos algunas variables para usar en las comparaciones
a = 10
b = 5
c = 15
d = 8

# Usamos el operador 'and'
# Ambas condiciones deben ser verdaderas para que el resultado sea True
resultado_and = (a > b) and (c > d)
print(f"Resultado de (a > b) and (c > d): {resultado_and}")
# (a > b) es True porque 10 > 5
# (c > d) es True porque 15 > 8
# True and True resulta en True

# Usamos el operador 'or'
# Al menos una de las condiciones debe ser verdadera para que el resultado sea True
resultado_or = (a < b) or (c > d)
print(f"Resultado de (a < b) or (c > d): {resultado_or}")
# (a < b) es False porque 10 no es menor que 5
# (c > d) es True porque 15 > 8
# False or True resulta en True

# Usamos el operador 'not'
# El operador 'not' invierte el valor de la expresión
resultado_not = not (a < b)
print(f"Resultado de not (a < b): {resultado_not}")
# (a < b) es False porque 10 no es menor que 5
# not False resulta en True

# Combinamos los operadores lógicos 'and', 'or', y 'not' en una sola expresión
resultado_combinado = (a > b) and (not (c < d)) or (b < d)
print(f"Resultado combinado: {resultado_combinado}")
# (a > b) es True porque 10 > 5
# (c < d) es False porque 15 no es menor que 8, y not (False) resulta en True
# (a > b) and (not (c < d)) es True because True and True resulta en True
# (b < d) es True porque 5 < 8
# True or True resulta en True






