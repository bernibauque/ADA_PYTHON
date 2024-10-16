import os
from pelicula_mexicana import Pelicula  # Asegúrate de importar la clase Pelicula

class CatalogoPelicula:
    def __init__(self, catalogo):
        self.nombre_catalogo = catalogo
        self.ruta_archivo = catalogo
        self.peliculas = []  # Inicializa la lista para almacenar las películas
        self.cargar_catalogo()  # Cargar el catálogo al inicializar

    def cargar_catalogo(self):  # Asegúrate de que este método esté correctamente indentado
        try:
            with open("peliculas_mexicanas.txt", 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(', ')
                    if len(datos) == 4:
                        nombre, director, año, genero = datos
                        pelicula = Pelicula(nombre, director, int(año), genero)  # Usa la clase Pelicula
                        self.peliculas.append(pelicula)
            print("Catálogo de películas cargado con éxito.")
        except FileNotFoundError:
            print("El archivo 'peliculas_mexicanas.txt' no existe.")
        except Exception as e:
            print(f"Error al cargar el catálogo: {e}")

    def agregar(self, pelicula):  # Método agregar
        try:
            with open(self.ruta_archivo, 'a') as archivo:
                archivo.write(f"{pelicula.get_nombre()}, {pelicula.getdirector()}, {pelicula.getaño()}, {pelicula.getgenero()}\n")
            self.peliculas.append(pelicula)  # Agrega la película a la lista
            print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")
        except Exception as e:
            print(f"Error al agregar la película: {e}")

    def listar(self):  # Método listar
        if not self.peliculas:
            print("El catálogo está vacío.")
            return

        print("Películas en el catálogo:")
        for pelicula in self.peliculas:
            print(f"{pelicula.get_nombre()}, {pelicula.getdirector()}, {pelicula.getaño()}, {pelicula.getgenero()}")

    def eliminar(self):
        try:
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre_catalogo}' eliminado.")
            self.peliculas.clear()  # Limpia la lista de películas
        except FileNotFoundError:
            print("El archivo del catálogo no existe.")
        except Exception as e:
            print(f"Error al eliminar el catálogo: {e}")