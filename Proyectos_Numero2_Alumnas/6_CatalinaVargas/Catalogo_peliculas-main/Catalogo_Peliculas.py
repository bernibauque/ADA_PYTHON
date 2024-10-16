"""Primero voy a importar el módulo OS que me permite hacer tareas como por ejemplo, trabajar con rutas y archivos, me da 
informacion del sistema y ejecutar comandos"""

import os

class Catalogo_Peliculas:
    
    """ Definimos el nombre de este catálogo (recordar, que es como la guía) y el objeto
        sería mi catálogo de pelicuas"""
    
    
    def __init__(self, nombre_catalogo):
        
        """Mi constructor, self es el catálogo específico y nombre_catalogo es un parámetro, o sea el nombre que le daré a mi catálogo."""
        
        self.nombre = nombre_catalogo   #almacena el nombre de mi catálogo
        
        self.ruta_del_archivo = f"{self.nombre}.txt"
        
    def agregar(self, pelicula):
        """En este caso el método, que es lo que puede hacer, es agregar una película""" 
        
        with open(self.ruta_del_archivo,'a') as archivo:
             archivo.write(pelicula + "\n")  #estamos agregando la película a mi archivo.
             
    def mostrar(self):
        """En este caso el método, que es lo que puede hacer, es mostrar una película""" 
        
        try:
            with open(self.ruta_del_archivo, 'r') as archivo: #Me permite abrir el archivo en modo lectura
                peliculas = archivo.readlines() # permite ller todas las líneas del archivo
                
                
                """Voy a crear un if para que recorra el archivo y me muestre las películas que haya en él; el except me ayuda a verificar si no hay un catálogo"""
                
                if peliculas: 
                    for pelicula in peliculas:
                        
                        print(f"\n La película que seleccionaste es:{pelicula}")
                               
                else:
                    print("No hay películas aún")
                    
        except FileNotFoundError:     #Me ayuda a evitar el error
            
            print("\n El catálogo no existe, debes agregar una peli primero")
            
    def eliminar(self):
        
        try:
            os.remove(self.ruta_del_archivo)
            print(f"El catálogo {self.nombre} ha sido eliminado")     
                   
        except FileNotFoundError:
            
            print("El catálogo no existe")    
            
    def menu(self):
        
        """Con mi Menú selecciono qué quiero hacer"""
        
        nombre_catalogo = input("Ingresa acá el nombre del catálogo que quieres crear: ")
        
        catalogo = Catalogo_Peliculas(nombre_catalogo)
        
        while True:
            print("Menú: ")
            print("1. Agregar película: ")
            print("2. Mostar película: ")
            print("3. Eliminar Catálogo: ")
            print("4. Salir ")
            
            opcion = input("Escoge la opción que quieres hacer hoy: ")
            
            """Voy a crear un if para que cada opción que escoja ejecute un código"""
            
            if opcion == "1":
                nombre_pelicula = input("ingrese el nombre de la película: ")
            
                catalogo.agregar(nombre_pelicula)
                
            elif opcion == "2":
                catalogo.mostrar()
                
                
            elif opcion == "3":
                catalogo.eliminar()
                
            elif opcion == "4":
                print("Gracias por visitarnos, ¡Vuelve pronto!")
                break
                
            else:
                print("Revisa tu selección, no es válida, elije nuevamente")
                
            
if __name__ == "__main__":
    catalogo = Catalogo_Peliculas("MiCatalogo")
    catalogo.menu()
            
                        
        
        