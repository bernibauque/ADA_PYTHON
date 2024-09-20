# Los tres modos de escritura en archivos:

# Modo 'w': Sobrescribir archivo
with open('modo_w.txt', 'w') as file:
    file.write('Este archivo fue sobrescrito usando el modo \'w\'.\n')
    file.write('Todo el contenido previo fue eliminado.\n')

print("Archivo 'modo_w.txt' creado con éxito.")

# Modo 'a': Añadir contenido al archivo existente
with open('modo_a.txt', 'a') as file:
    file.write('Este texto se añadió al final del archivo usando el modo \'a\'.\n')
    file.write('El contenido previo no fue eliminado.\n')

print("Archivo 'modo_a.txt' creado o modificado con éxito.")

# Modo 'x': Crear un archivo nuevo
# Nota: Si el archivo ya existe, este código fallará y no se creará el archivo.
with open('modo_x.txt', 'x') as file:
    file.write('Este archivo fue creado usando el modo \'x\'.\n')
    file.write('Falla si el archivo ya existe.\n')

print("Archivo 'modo_x.txt' creado con éxito.")


