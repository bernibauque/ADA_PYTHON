import math

# Solicitar al usuario un número decimal
numero = float(input("Ingresa un número decimal: "))

# Redondear al entero superior e inferior
ceil_valor = math.ceil(numero)
floor_valor = math.floor(numero)

# Calcular la raíz cuadrada
raiz_cuadrada = math.sqrt(numero)

# Si el número es entero positivo, calcular el factorial
if numero.is_integer() and numero >= 0:
    factorial = math.factorial(int(numero))
else:
    factorial = "No se puede calcular el factorial de un número decimal o negativo."

# Elevar el número a la potencia de otro número
potencia = float(input("Ingresa un número para elevar a la potencia: "))
resultado_potencia = math.pow(numero, potencia)

# Mostrar resultados
print(f"Valor redondeado hacia arriba: {ceil_valor}")
print(f"Valor redondeado hacia abajo: {floor_valor}")
print(f"Raíz cuadrada: {raiz_cuadrada}")
print(f"Factorial (si aplica): {factorial}")
print(f"Resultado de elevar {numero} a la potencia de {potencia}: {resultado_potencia}")
