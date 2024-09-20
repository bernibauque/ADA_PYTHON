import csv  # Importar el módulo csv para trabajar con archivos CSV

# Definir los nombres de las columnas para el archivo CSV
# Estos nombres deben coincidir con las claves de los diccionarios que se escribirán en el archivo
fieldnames = ['Nombre', 'Edad', 'Ciudad']

# Abrir el archivo CSV en modo escritura
# 'w' indica que se está abriendo el archivo en modo escritura
# 'newline=""' se utiliza para evitar líneas en blanco adicionales en algunos sistemas operativos
with open('archivo.csv', 'w', newline='') as file:
    # Crear un objeto DictWriter
    # Se pasa el archivo y la lista de nombres de columnas (fieldnames)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Escribir la fila de encabezado en el archivo CSV
    # Esto crea la primera fila con los nombres de las columnas
    writer.writeheader()
    
    # Escribir una fila de datos en el archivo CSV
    # Cada diccionario debe tener claves que coincidan con los nombres de las columnas
    writer.writerow({'Nombre': 'Ana', 'Edad': '30', 'Ciudad': 'Madrid'})
    
    # Escribir múltiples filas de datos en el archivo CSV
    # Cada diccionario en la lista debe tener claves que coincidan con los nombres de las columnas
    writer.writerows([
        {'Nombre': 'Luis', 'Edad': '25', 'Ciudad': 'Barcelona'},
        {'Nombre': 'Marta', 'Edad': '28', 'Ciudad': 'Valencia'}
    ])
