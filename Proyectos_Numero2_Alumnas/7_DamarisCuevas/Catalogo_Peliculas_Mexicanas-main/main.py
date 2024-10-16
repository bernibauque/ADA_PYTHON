from pelicula_mexicana import Pelicula
from catalogo_peliculas_mexicanas import CatalogoPelicula

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo")
    print("4. Salir")

def main():
    catalogo = CatalogoPelicula("catalogo_peliculas")

    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))  # Convertir la entrada a entero

        if opcion == 1:  # Comparar con enteros
            nombre = input("Ingresa el nombre de la película: ")
            director = input("Ingresa el director de la película: ")
            año = int(input("Ingresa el año de la película: "))
            genero = input("Ingresa el género de la película: ")
            pelicula = Pelicula(nombre, director, año, genero)
            catalogo.agregar(pelicula)
        elif opcion == 2:
            catalogo.listar()
        elif opcion == 3:
            catalogo.eliminar()
        elif opcion == 4:
            print("Saliste del catálogo")
            break
        else:
            print("Esta opción no es válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()