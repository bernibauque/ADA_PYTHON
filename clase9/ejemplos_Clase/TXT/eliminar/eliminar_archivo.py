import os # importamos modulo

# definimos el nombre del archivo
nombre_archivo = 'archivo.txt'

#comprobar si el archivo existe en la ruta especificada
#la funcion os.path.exists() devuelve True si el archivo existe
#false en caso contrario
if os.path.exists(nombre_archivo):
    #si el archivo existe, procedera a eliminarlo
    #la funcion os.remove() elimina el archivo en la ruta especificada
    os.remove(nombre_archivo)
    print(f'Archivo "{nombre_archivo}" eliminado. ')
else:
    #si el archivo no existe, informar al usuario que no se encontro nada
    print(f'El Archivo "{nombre_archivo}" no existe. ')
