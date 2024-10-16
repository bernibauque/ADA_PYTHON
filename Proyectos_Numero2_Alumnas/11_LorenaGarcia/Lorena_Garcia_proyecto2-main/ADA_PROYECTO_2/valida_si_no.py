
print("¿Deseas agregar otra pelicula? SI/NO")
otra = input()
if otra.lower()in ["si"]:
    from AgregarPeli import agregar
    agregar()
else: 
    otra.lower() in ["no"]
    print("Ok, gracias, adiosito!")