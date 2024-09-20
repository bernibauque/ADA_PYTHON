# Escribe un programa que verifique si un número es par o impar usando el operador ternario. 
# Imprime "Par" si el número es divisible por 2 y "Impar" si no lo es.

# Solicita un número al usuario
numero = int(input("Introduce un número: "))

# Usa el operador ternario para verificar si es par o impar
resultado = "Par" if numero % 2 == 0 else "Impar"

print(resultado)
