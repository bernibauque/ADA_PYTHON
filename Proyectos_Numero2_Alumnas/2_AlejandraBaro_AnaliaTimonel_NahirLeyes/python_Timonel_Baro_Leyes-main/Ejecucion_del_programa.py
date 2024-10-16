from Catalogo_Pelis import CatalogoPelicula, Pelicula       #importamos las clases que realizamos en el modulo de catalogo_pelis para ejecutar el programa

print('\"BIENVENIDO A TU CATALOGO DE PELICULAS!!!\"')
print()

def mostrar_menu():     #creamos un menu para que el usuario elija que accion realizar
    print("\nSelecciona una opción:")
    print("1. Agregar una película")
    print("2. Listado de películas")
    print("3. Eliminar el catálogo")
    print("4. Salir")

def main():
    nombre_catalogo = input("Por favor ingresa el nombre del catálogo de películas: ")
    catalogo = CatalogoPelicula(nombre_catalogo)#llamamos a la clase para que el programa opere correctamente la opcion que elija el usuario

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la película: ")
            director = input("Director: ")
            genero = input("Género: ")
            pelicula = Pelicula(nombre, director, genero)
            catalogo.agregar(pelicula)
        elif opcion == '2':
            catalogo.listar()
        elif opcion == '3':
            catalogo.eliminar()
        elif opcion == '4':
            print("Saliendo del programa...\n GRACIAS!!")
            break
        else:
            print("La opción no es válida. Intentalo nuevamente.")

if __name__ == "__main__":
    main()              