# Escribe un programa que clasifique a una persona en una categoría según su edad. 
# Usa un condicional if tradicional con operadores lógicos (and, or) para las siguientes categorías:
# "Niño" si la edad está entre 0 y 12 años.
# "Adolescente" si la edad está entre 13 y 19 años.
# "Adulto" si la edad está entre 20 y 64 años.
# "Adulto Mayor" si la edad es 65 o más.

# Solicita la edad al usuario
edad = int(input("Introduce tu edad: "))

# Clasifica la edad en diferentes categorías
if 0 <= edad <= 12:
    categoria = "Niño"
elif 13 <= edad <= 19:
    categoria = "Adolescente"
elif 20 <= edad <= 64:
    categoria = "Adulto"
else:
    categoria = "Adulto Mayor"

print(f"Categoría: {categoria}")
