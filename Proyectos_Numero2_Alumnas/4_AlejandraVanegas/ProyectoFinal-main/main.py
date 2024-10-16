# main.py

from catalogo_pelicula import CatalogoPelicula
from pelicula import Pelicula

def main():
    print("Bienvenido al Gestor de Catálogo de Películas")
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ").strip()
    if not nombre_catalogo:
        print("El nombre del catálogo no puede estar vacío. Se usará 'DefaultCatalogo'.")
        nombre_catalogo = "DefaultCatalogo"
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar Catálogo de Películas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            nombre_pelicula = input("Ingrese el nombre de la película: ").strip()
            if nombre_pelicula:
                pelicula = Pelicula(nombre_pelicula)
                catalogo.agregar(pelicula)
            else:
                print("El nombre de la película no puede estar vacío.")
        elif opcion == '2':
            catalogo.listar()
        elif opcion == '3':
            confirmacion = input(f"¿Está seguro de eliminar el catálogo '{nombre_catalogo}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                catalogo.eliminar()
                print("Programa finalizado.")
                break  # Salimos del programa después de eliminar el catálogo
            else:
                print("Eliminación cancelada.")
        elif opcion == '4':
            print("Gracias por usar el Gestor de Catálogo de Películas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()