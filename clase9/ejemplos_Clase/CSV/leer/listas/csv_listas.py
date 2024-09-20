import csv #Importamos modulo

#Abrir el archivo csv en modo lectura
with open('archivo.csv', 'r') as file:
    #crear un lector csv que interpreta el archivo como un archivo csv
    reader = csv.reader(file)

    #iterar sobre cada fila del archivo csv
    for fila in reader:
        print(fila) #Imprimir cada fila como una lista de cadenas