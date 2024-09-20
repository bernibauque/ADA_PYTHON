# Lista de números predefinida
numeros = [10, 20, 30, 40, 50, 60]
print(f"La lista de numeros definida es: {numeros}")

# Pedir al usuario que ingrese el índice de inicio y fin para la sublista
inicio = int(input("Ingrese el índice de inicio de la sublista: "))
fin = int(input("Ingrese el índice de fin de la sublista: "))

# Obtener la sublista usando slicing
sublista = numeros[inicio:fin]

# Sumar los elementos de la sublista
suma_sublista = sum(sublista)

# Mostrar la suma de la sublista
print(f"La suma de la sublista es: {suma_sublista}")
