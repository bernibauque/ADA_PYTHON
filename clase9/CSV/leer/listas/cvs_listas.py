import csv  # Importa el módulo csv que permite trabajar con archivos CSV

# Abrir el archivo CSV en modo lectura
with open('archivo.csv', 'r') as file:
    # Crear un lector CSV que interpreta el archivo como un archivo CSV
    reader = csv.reader(file)
    
    # Iterar sobre cada fila del archivo CSV
    for fila in reader:
        print(fila)  # Imprimir cada fila como una lista de cadenas


