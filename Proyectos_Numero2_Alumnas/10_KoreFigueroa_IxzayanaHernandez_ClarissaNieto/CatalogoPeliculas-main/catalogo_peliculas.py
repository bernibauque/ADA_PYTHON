import os # Creamos una navegación de directorios con ayuda de la función os 

from pelicula import Pelicula # Importar clase Pelicula del archivo pelicula.py
  
class CatalogoPelicula: # Nombrar una nueva clase 
    def __init__(self, nombre): # Definir atributo 
        self.nombre = nombre  # Nombre del catálogo, llama a la función del atributo 
        self.ruta_archivo = f"{nombre}.txt"  # Ruta del archivo donde se guardarán las películas 
        self._crear_catalogo_si_no_existe()  # Se crea un catalogo en el caso de no coincidir con la respuesta del usuario

    def _crear_catalogo_si_no_existe(self): # Se define atributo para verificar si el archivo existe
        if not os.path.exists(self.ruta_archivo): #Comprobar si existe el archivo
            with open(self.ruta_archivo, 'w') as archivo: # Se crea o se abre el archivo 
                pass  # Solo crea un archivo vacío si no existe 

    def agregar(self, pelicula): #Atributo para agregar películas al catalogo 
        try: # Usamos try/except para manejar errores
            with open(self.ruta_archivo, 'a') as archivo: # Abre el archivo y permite agregar contenido
                archivo.write(pelicula.nombre + '\n')  # Agrega el nombre de la película al archivo 
        except Exception as e: 
            print(f"Error al agregar la película: {e}") # Para indicar que no se logró agregar la pelicula

    def listar(self): # Atributo para enlistar las películas 
        try: 
            if os.path.exists(self.ruta_archivo): # Comprobar si el archivo existe
                with open(self.ruta_archivo, 'r') as archivo: # Abre el archivo para lectura
                    peliculas = archivo.readlines()  # Lee y guarda todas las líneas del archivo 
                return [pelicula.strip() for pelicula in peliculas]  # Elimina saltos de línea 
            return []  # Retorna una lista vacía si no existe el archivo 
        except Exception as e: # La variable e tendrá un mensaje que describe lo que salió mal. 
            print(f"Error al listar las películas: {e}") 
            return [] 

    def eliminar(self): # Atributo para eliminar archivos
        try: 
            if os.path.exists(self.ruta_archivo): # Comprobar si el archivo existe
                os.remove(self.ruta_archivo)  # Elimina el archivo del catálogo 
        except Exception as e: 
            print(f"Error al eliminar el catálogo: {e}") 

def menu(catalogo): # Atributo de menú 
    while True: # Bucle para opciones de menú 
        print("\nMenú de Opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar Catálogo de Películas")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ") # Interaccion con el usuario para elegir una opción del menu

        if opcion == '1': # Condicion 1 para agregar películas 
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            nueva_pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(nueva_pelicula) # Usa el nuevo nombre
            print(f"Película '{nueva_pelicula.nombre}' agregada al catálogo.")
        
        elif opcion == '2': #Condicion 2 para enlistar las peliculas
            print("Películas en el catálogo:")
            peliculas = catalogo.listar() # Lista las películas
            if peliculas:
                for p in peliculas:
                    print(f"- {p}") # Muestra cada película
            else:
                print("No hay películas en el catálogo.") #En caso de no haber películas 
        
        elif opcion == '3': # Condicion 3 Eliminar catalogos 
            confirmacion = input("¿Está seguro de que desea eliminar el catálogo? (sí/no): ")
            if confirmacion.lower() == 'si':
                catalogo.eliminar() # Elimina el catálogo
                print("Catálogo de películas eliminado.")
                break # Sale del menú después de eliminar
        
        elif opcion == '4': # Condicion 4 para salir del programa 
            print("Bye Bye")
            break # Termina el programa
        
        else: # Condicion en caso de no seleccionar una opción correctamente 
            print("Opción no válida. Por favor, intenta nuevamente.")

def main(): #Definir funcion principal 
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPelicula(nombre_catalogo) # Crea una instancia de CatalogoPelicula

    menu(catalogo) # Llamar a la función, muestra el menú para interactuar

if __name__ == "__main__":
    main() # Llama a la función main si el archivo se ejecuta directamente