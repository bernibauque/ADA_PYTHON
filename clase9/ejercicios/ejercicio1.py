# Leer archivo usando readlines()
with open('mi_archivo.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print(linea.strip())  # strip() elimina saltos de línea extra
