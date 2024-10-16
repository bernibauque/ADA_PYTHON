from pelicula import *

def obtener_opcion_valida():
    while True:
        try:
            opcion = int(input('Escriba una opción del menú (del 1 al 4): '))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, ingrese un número entre 1 y 4.")
        except ValueError:
            print('Por favor, ingrese un número válido.')


nombre_catalogo = input('Ingrese el nombre del catálogo: \n')
# Creación del objeto 
catalogo = CatalogoPelicula(nombre_catalogo)

while True:
        print("\nOpciones: ")
        print("1. Agregar película")
        print("2. Listar película")
        print("3. Eliminar catálogo de películas")
        print("4. SALIR\n")

        opcion = obtener_opcion_valida()
        
        # OPCIÓN 1: Agregar película.
        if opcion == 1:
            nombre_pelicula = input('Escribe el nombre de la película: ').strip()
            if nombre_pelicula:
                pelicula = Pelicula(nombre_pelicula)
                try:
                    catalogo.agregar_pelicula(pelicula)
                    print(f"Película '{nombre_pelicula} agregada al catálogo")
                except Exception as e:
                    print(f'Error al agregar la película: {e}')
            else:
                print('Error: El nombre de la película no puede estar vacío.')

        # OPCIÓN 2: Listar película.
        elif opcion == 2:
            try: 
                catalogo.listar_peliculas()
            except FileNotFoundError:
                print("Error: El archivo del catálogo no existe. Agregar películas primero.")
            except Exception as e:
                print(f'Error al listar las películas: {e}')

        # OPCIÓN 3: Eliminar catálogo de películas.
        elif opcion == 3:
            confirmacion = input('¿Estas seguro de que quieres eliminar el catálogo? (s/n): ').lower()
            if confirmacion == 's':
                try:
                    catalogo.eliminar_catalogo()
                    print('Catálogo eliminado.')
                except FileNotFoundError:
                        print('Error: El archivo del catálogo no existe.')
                except Exception as e:
                        print(f'Error al eliminar el catálogo: {e}')
            else:
                print('Operación de eliminación cancelada.')

        # OPCIÓN 4: SALIR
        elif opcion == 4:
            print('Saliendo del programa. ¡Hasta luego!') # Mensaje de despedida.
            break 

        input('\nPresione Enter para continuar.')