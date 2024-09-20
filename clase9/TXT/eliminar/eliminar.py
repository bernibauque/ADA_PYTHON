# Importar el módulo 'os' para interactuar con el sistema operativo
import os

# Definir el nombre del archivo que queremos eliminar
nombre_archivo = 'archivo.txt'

# Comprobar si el archivo existe en la ruta especificada
# La función os.path.exists() devuelve True si el archivo existe, False en caso contrario
if os.path.exists(nombre_archivo):
    # Si el archivo existe, proceder a eliminarlo
    # La función os.remove() elimina el archivo en la ruta especificada
    os.remove(nombre_archivo)
    # Informar al usuario que el archivo ha sido eliminado
    print(f'Archivo "{nombre_archivo}" eliminado.')
else:
    # Si el archivo no existe, informar al usuario que no se encontró el archivo
    print(f'El archivo "{nombre_archivo}" no existe.')





