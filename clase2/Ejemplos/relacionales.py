# Definimos dos variables para comparar
a = 10
b = 5

# Igual a
resultado_igual = (a == b)
print(f"¿{a} es igual a {b}? {resultado_igual}")  # False, porque 10 no es igual a 5

# No igual a
resultado_no_igual = (a != b)
print(f"¿{a} es diferente de {b}? {resultado_no_igual}")  # True, porque 10 es diferente de 5

# Mayor que
resultado_mayor_que = (a > b)
print(f"¿{a} es mayor que {b}? {resultado_mayor_que}")  # True, porque 10 es mayor que 5

# Menor que
resultado_menor_que = (a < b)
print(f"¿{a} es menor que {b}? {resultado_menor_que}")  # False, porque 10 no es menor que 5

# Mayor o igual que
resultado_mayor_o_igual = (a >= b)
print(f"¿{a} es mayor o igual que {b}? {resultado_mayor_o_igual}")  # True, porque 10 es mayor que 5

# Menor o igual que
resultado_menor_o_igual = (a <= b)
print(f"¿{a} es menor o igual que {b}? {resultado_menor_o_igual}")  # False, porque 10 no es menor ni igual a 5

