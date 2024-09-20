import os

nombre_archivo = 'archivo_para_eliminar.txt'

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(f'Archivo "{nombre_archivo}" eliminado.')
else:
    print(f'El archivo "{nombre_archivo}" no existe.')
