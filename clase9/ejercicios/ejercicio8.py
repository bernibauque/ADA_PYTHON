numero = int(input("Ingresa un número entre 1 y 10: "))

if numero < 1 or numero > 10:
    raise ValueError("El número debe estar entre 1 y 10.")
else:
    print(f"Número ingresado: {numero}")
