# catalogo_pelicula.py

import os
from pelicula import Pelicula

class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{self.nombre}.txt"
        # Si el archivo no existe, lo creamos
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                pass  # Crear un archivo vacío
            print(f"Catálogo '{self.nombre}' creado exitosamente.")
        else:
            print(f"Catálogo '{self.nombre}' cargado exitosamente.")

    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(pelicula.get_nombre() + '\n')
        print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            print("El catálogo no existe.")
            return
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            peliculas = archivo.readlines()
            print(f"DEBUG: Se encontraron {len(peliculas)} películas en el archivo.")
            if not peliculas:
                print("No hay películas en el catálogo.")
                return
            print("\nPelículas en el catálogo:")
            for idx, pelicula in enumerate(peliculas, start=1):
                print(f"{idx}. {pelicula.strip()}")

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre}' eliminado.")
        else:
            print("El catálogo no existe.")