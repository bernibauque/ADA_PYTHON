# Lista de nombres
nombres = ["Ana", "Luis", "Carlos", "Pedro", "María"]

# Iterar usando enumerate
for index, nombre in enumerate(nombres):
    if nombre.startswith("A"):
        continue  # Saltar nombres que empiezan con 'A'
    if nombre == "Carlos":
        print(f"Nombre 'Carlos' encontrado en el índice {index}. Se detiene la búsqueda.")
        break
    print(f"Índice {index}: Nombre '{nombre}'")
