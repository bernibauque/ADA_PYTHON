# Importar el modulo
import csv

# Abrimos el archivo csv en modo lectura
with open('archivo2.csv', 'r') as file:
    #Creamos el lector de diccionario que procesa un archivo csv
    #el lector convierte cada fila en un diccionario usando los
    #encabezados de columnas como claves
    reader = csv.reader(file)

    #iterar sobre cada fila del archivo csv
    for fila in reader:
        print(fila) #imprimimos cada fila como diccionario