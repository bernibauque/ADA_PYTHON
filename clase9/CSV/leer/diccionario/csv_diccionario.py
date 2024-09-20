# Importa el módulo csv, que proporciona 
# herramientas para trabajar con archivos CSV
import csv  

# Abrir el archivo CSV en modo lectura
with open('archivo2.csv', 'r') as file:
    # Crear un lector CSV de diccionario que procesa el archivo CSV
    # El lector convierte cada fila en un diccionario usando los 
    # encabezados de columna como claves
    reader = csv.DictReader(file)
    
    # Iterar sobre cada fila del archivo CSV
    for fila in reader:
        print(fila)  
# Imprimir cada fila como un diccionario donde las claves son los 
# encabezados de columna y los valores son los datos




