try:
    numero = int(input("Ingresa un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: Debes ingresar un número válido.")
