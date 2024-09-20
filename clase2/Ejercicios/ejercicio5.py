# Escribe un programa que verifique si un número es positivo, negativo o cero usando el operador ternario 
# en una sola línea de código para cada estado y muestra el resultado.

# Solicita un número al usuario
numero = float(input("Introduce un número: "))

# Usa el operador ternario para determinar el estado del número
estado = "Positivo" if numero > 0 else "Negativo" if numero < 0 else "Cero"

print(f"El número es: {estado}")
