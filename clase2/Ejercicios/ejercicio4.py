# Escribe un programa que calcule el precio final de un producto después de aplicar un descuento del 15% 
# si el precio inicial es mayor a 200. Usa un condicional if tradicional para aplicar el descuento y muestra el precio final.

# Solicita el precio inicial del producto
precio_inicial = float(input("Introduce el precio inicial del producto: "))

# Aplica el descuento si el precio es mayor a 200
if precio_inicial > 200:
    descuento = precio_inicial * 0.15
    precio_final = precio_inicial - descuento
else:
    precio_final = precio_inicial

print(f"El precio final es: {precio_final:.2f} pesos.")
