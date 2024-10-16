#Implementación de la clase CatálogoPelicula
#Esta es la clase que va a gestionar todo el catálogo de películas
#Gestionar operaciones como agregar, listar y eliminar películas del catálogo.
#Atributos: nombre: El nombre del catálogo y 
#ruta_archivo: La ruta del archivo donde se va a guardar el catálogo.

import os #Importamos os para manejar archivos
from Pelicula import Pelicula # importamos la clase película

class CatálogoPelícula:
    #Constructor
    def __init__(self, título_catálogo): 
        self.nombre= título_catálogo #Atributo
        self.ruta_archivo= f'{título_catálogo}.txt' #Debería abrir un archivo con el atributo

#Método agregar 'add' open(self.ruta_archivo, 'a')
    def agregar(self,película):  #Agregar
        with open(self.ruta_archivo, 'a') as file: #Se crea y agrega 
            file.write(f'{película.título}, {película.director}, {película.año} \n') #imprimen los detalles de la película agregada

    def listar(self): #listar
        try:
         with open(self.ruta_archivo, 'r') as file: #Abrir un archivo para leerlo ('r') o en modo lectura
          películas= file.readlines() #para leer todas las líneas del archivo creado anteriormente
          if películas: # creamos un if para el caso en que exista o no el archivo en el catálogo
             print('\nPelículas en este catálogo') #imprime mensaje
             for línea in películas: #que se repita frecuentemente la función
                título, director, año= línea.strip().split(',') # Separa y ordena todo en la línea
                print(f'Título:{título}, Director:{director}, Año: {año}') #Ya con esto se imprimen las películas que están en el catálogo con los mismos atributos
          else: #en caso contrario
            print('\nEste catálogo está vacío') #se imprime el mensaje
        except FileNotFoundError: #creamos una función para que no se corte o detenga el código 
           print('\nEl catálogo no existe. Necesitas agregar una película.')


    def eliminar(self): #eliminar
       try:
          os.remove(self.ruta_archivo) #intentemos elminar el archivo
          print('\nYa ha sido eliminado el catálogo') #imprimimos mensaje
       except FileNotFoundError: #creamos una función para que no se corte o detenga el código 
            print('\nEl catálogo no existe. No se puede eliminar') #imprimimos mensaje