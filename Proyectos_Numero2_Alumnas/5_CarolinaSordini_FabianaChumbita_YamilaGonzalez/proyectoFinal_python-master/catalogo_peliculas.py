
import json
from pelicula import Pelicula

class CatalogoPelicula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.json"


    def agregar(self, pelicula):
        try:
            peliculas = self._cargar_catalogo()
            peliculas.append(pelicula.obtener_nombre())
            with open(self.ruta_archivo, 'w') as archivo:
                json.dump(peliculas, archivo, indent=4)
            print(f"Película '{pelicula.obtener_nombre()}' agregada al catálogo.")
        except Exception as e:
            print(f"Error al agregar la película: {e}")

  
    def listar(self):
        try:
            peliculas = self._cargar_catalogo()
            if peliculas:
                print("Catálogo de Películas:")
                for i, pelicula in enumerate(peliculas, start=1):
                    print(f"{i}. {pelicula}")
            else:
                print("El catálogo está vacío.")
        except FileNotFoundError:
            print("El catálogo no existe.")

  
    def eliminar(self):
        try:
            open(self.ruta_archivo, 'w').close()  
            print(f"Catálogo '{self.nombre}' vaciado.")
        except Exception as e:
            print(f"Error al eliminar el catálogo: {e}")


    def _cargar_catalogo(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Vaciar catálogo")
    print("4. Salir")

def main():
    catalogo = CatalogoPelicula("mi_catalogo")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            nombre_pelicula = input("Introduce el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(pelicula)
        elif opcion == '2':
            catalogo.listar()
        elif opcion == '3':
            catalogo.eliminar()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
