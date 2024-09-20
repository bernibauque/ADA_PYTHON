# Creamos un diccionario
persona = {
    "nombre" : "Analia",
    "edad" : 36, 
    "ciudad" : "Colon - Entre Rios"
}

# Usamos el metodos values
valores = persona.values()

# Imprimimos
print("Valores del diccionario: ", valores)

# Convertir valores en una lista
valores_lista = list(valores)
print("Valores como lista: ", valores_lista)