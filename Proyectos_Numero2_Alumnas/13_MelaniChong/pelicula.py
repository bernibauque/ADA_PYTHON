import os 

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre # Atributo privado
    def __str__(self):
        return f"nombre:{self.nombre}"

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

class CatalogoPelicula:

    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archvio = f'{self.nombre}.txt'

    def agregar_pelicula(self, pelicula):
        with open (self.ruta_archvio, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.ruta_archvio, 'r') as archivo:
            print(archivo.read()) # Muestra lo que se encuentra dentro del archivo txt

    def eliminar_catalogo(self):
        os.remove(self.ruta_archvio)
        print(f'Catálogo eliminado: {self.ruta_archvio}')