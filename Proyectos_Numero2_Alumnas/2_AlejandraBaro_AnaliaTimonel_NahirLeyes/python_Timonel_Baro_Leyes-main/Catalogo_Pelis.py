import os #modulo para poder eliminar archivo

class Pelicula:             #definimos una clase con atributo privado
    def __init__(self, nombre, director, genero):
        self.__nombre = nombre
        self.director = director
        self.genero = genero

    @property   #utilizamos un decorador para acceder al atributo __nombre
    def nombre(self):
        return self.__nombre
    
    @nombre.setter  #utilizamos decorador para asignar otro valor a nombre
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")  #detenemos la ejecucion del programa si el usuario ingresa espacios vacios

    def __str__(self):
        return f"{self.__nombre} Dirigida por: {self.director} Género: {self.genero}"   #retornamos los datos de nuestra clase
    

    
class CatalogoPelicula:     #Definimos la clase de catalogo de peliculas 
    ruta_archivo = "Pelis.txt"      #definimos la variable con el nombre de donde se almacenara el catalogo de pelicula
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{self.nombre}.txt"
        self.peliculas = self.cargar_peliculas()

    def cargar_peliculas(self):
        peliculas = []
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    nombre, director, genero = linea.strip().split(',')     #utilizamos algunos mmetodos str para mejorar el orden de escritura
                    peliculas.append(Pelicula(nombre, director, genero))
        except FileNotFoundError:
            print(f"El archivo '{self.ruta_archivo}' no existe. Se creará un nuevo catálogo.")
        return peliculas

    def guardar_peliculas(self):
        with open(self.ruta_archivo, 'w') as archivo:       #abrimos el archivo y escribimos los datos de cada pelicula
            for pelicula in self.peliculas:
                archivo.write(f"{pelicula.nombre},{pelicula.director},{pelicula.genero}\n")

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)     #abrimos el archivo y agregamos la pelicula
        self.guardar_peliculas()

    def listar(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            for pelicula in self.peliculas:
                print(pelicula)

    def eliminar(self):
        try:
            os.remove(self.ruta_archivo)        #utilizamos os.remove para eliminar el archivo
            self.peliculas = []
            print(f"El catálogo '{self.nombre}' fue eliminado.")
        except FileNotFoundError:     
            print(f"El catálogo '{self.nombre}' no existe.")