import csv

with open('datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
