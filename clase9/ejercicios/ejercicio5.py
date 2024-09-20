import csv

with open('alumnos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])
    escritor.writerow(["Ana", 23])
    escritor.writerow(["Luis", 25])
