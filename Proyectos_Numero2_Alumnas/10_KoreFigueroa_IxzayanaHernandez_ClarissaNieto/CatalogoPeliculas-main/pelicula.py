# PROYECTO FINAL - CATALOGO DE PELICULAS
# Objetivo: crear un catálogo de películas que le permita al usuario interactuar en un archivo de texto para agregar, listar y eliminar películas del catálogo
# Creado por Koré Figueroa, Ixzayana Hernández y Clarissa Nieto

class Pelicula: # Crear y nombrar clase Pelicula
    def __init__(self, nombre):  # Constructor que recibe el nombre de la película 
        self.__nombre = nombre  # Almacena el nombre de la película de forma privada 
    
    @property # Usamos este comando para convertir a propiedad y acceder al atributo
    def nombre(self):  # Método para acceder al nombre de manera controlada 
        return self.__nombre # Devuelve el valor del atributo