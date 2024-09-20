# Crear un diccionario
persona = {
    "nombre" : "Emilia",
    "edad" : 33,
    "ciudad" : "CABA",
    "profesion" : "Veterinaria"
}

# Imprimir el diccionario original
print("Diccionario original: ", persona)

#Usamos popItem para eliminar y obtener el ultimo par clave-valor
ultimo_elemento = persona.popitem()

#Imprimimos el par clave-valor
print("Ultimo par clave-valor eliminado: ", ultimo_elemento)

#Imprimimos despues de usar popItem
print("Diccionario despues de usar popItem: ", persona)
