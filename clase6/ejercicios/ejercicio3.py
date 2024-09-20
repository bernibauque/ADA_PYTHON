# Lista de cadenas
cadenas = ["", "Hola", "Mundo", "Python", "Es", "Genial"]

# Iterar usando enumerate
for index, cadena in enumerate(cadenas):
    if cadena == "":
        continue  # Saltar cadenas vacías
    if len(cadena) > 5:
        print(f"Cadena '{cadena}' excede los 5 caracteres. Se detiene la búsqueda.")
        break
    print(f"Índice {index}: Cadena '{cadena}'")
