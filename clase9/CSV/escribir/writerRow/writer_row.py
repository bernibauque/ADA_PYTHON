import csv  # Importar el módulo csv para trabajar con archivos CSV

# Definir los nombres de las columnas para el archivo CSV
fieldnames = ['Nombre', 'Edad', 'Ciudad']

# Abrir el archivo CSV en modo escritura
# 'w' indica que se está abriendo el archivo en modo escritura
# 'newline=""' se utiliza para evitar líneas en blanco adicionales en algunos sistemas operativos
with open('archivo.csv', 'w', newline='') as file:
    # Crear un objeto writer
    # Se pasa el archivo y la lista de nombres de columnas (fieldnames)
    writer = csv.writer(file)
    
    # Escribir la fila de encabezado en el archivo CSV
    # Esto crea la primera fila con los nombres de las columnas
    writer.writerow(fieldnames)
    
    # Escribir una fila de datos en el archivo CSV
    # Cada elemento en la lista representa un valor en una celda de la fila
    writer.writerow(['Ana', '30', 'Madrid'])
    
    # Escribir otra fila de datos en el archivo CSV
    writer.writerow(['Luis', '25', 'Barcelona'])
    
    # Escribir una fila más de datos en el archivo CSV
    writer.writerow(['Marta', '28', 'Valencia'])







