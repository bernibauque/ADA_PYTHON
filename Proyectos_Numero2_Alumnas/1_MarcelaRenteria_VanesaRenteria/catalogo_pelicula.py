# catalogo_pelicula.py
#Equipo: Elsie Vanessa Ensaldo Renteria & Marcela Kristel Ensaldo Renteria


import os  # Módulo para manipulación de archivos
from pelicula import Pelicula  # Importar la clase Pelicula

class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.nombre_catalogo = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"

    # Método para agregar una película al archivo
    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:  # 'a' es para agregar
            archivo.write(pelicula.obtener_nombre() + '\n')
        print(f"Película '{pelicula.obtener_nombre()}' agregada al catálogo.")

    # Método para listar las películas en el archivo
    def listar(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as archivo:  # 'r' es para leer
                print("Catálogo de películas:")
                print(archivo.read())
        else:
            print("El catálogo no existe o está vacío.")

    # Método para eliminar el archivo del catálogo
    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"El catálogo '{self.nombre_catalogo}' ha sido eliminado.")
        else:
            print("El catálogo no existe.")
