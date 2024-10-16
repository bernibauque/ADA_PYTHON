# main.py
# Equipo: Elsie Vanessa Ensaldo Renteria & Marcela Kristel Ensaldo Renteria


from catalogo_pelicula import CatalogoPelicula
from pelicula import Pelicula

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo")
    print("4. Salir")

def main():
    # Crear una instancia del catálogo
    nombre_catalogo = input("Introduce el nombre del catálogo: ")
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            # Opción para agregar una película
            nombre_pelicula = input("Introduce el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(pelicula)
        elif opcion == '2':
            # Opción para listar películas
            catalogo.listar()
        elif opcion == '3':
            # Opción para eliminar el catálogo
            catalogo.eliminar()
        elif opcion == '4':
            # Opción para salir
            print("Saliendo del programa. ¡Gracias por usar el catálogo de películas!")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()
