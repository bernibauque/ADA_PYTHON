import csv

# definimos los nombres de las columnas para el archivo csv
fieldnames = ['Nombre', 'Edad', 'Ciudad']

#newline='' se utiliza para evitar lineas en blanco adicionales en algunos S.O
with open('archivo.csv', 'w', newline='') as file:
    #Creamos un objeto DictWriter
    #se pasa el archivo y la lista de nombres de columnas(fieldnames)
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    #escribir la fila de encabezados en el archivo csv
    #esto crea la primera fila con los nombres de columnas
    writer.writeheader()

    #escribir una fila con los datos de un archivo csv
    #cada diccionario debe tener claves que coincidan con los nombres de las columnas
    writer.writerow({'Nombre' : 'Ana', 'Edad' : '35', 'Ciudad' : 'Neuquen'})

    #escribir multiples filas de datos en el archivo csv
    writer.writerows([
        {'Nombre' : 'Julia', 'Edad' : '35', 'Ciudad' : 'Neuquen'},
        {'Nombre' : 'Mario', 'Edad' : '35', 'Ciudad' : 'Neuquen'}
    ])