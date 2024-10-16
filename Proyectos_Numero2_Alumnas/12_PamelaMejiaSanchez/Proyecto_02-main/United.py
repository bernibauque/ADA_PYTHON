#Unimos todo el cuerpo del programa, invocando el código
# de Catálogo y Película

from Catálogo import CatálogoPelícula
from Pelicula import Pelicula

def united():
    nombre_catálogo=input('Ingresa el nombre del catálogo: (escribe el nombre que quieras) \n')
    catalogo=CatálogoPelícula(nombre_catálogo) #Creamos una instancia de Catálogo película

#Hay que hacer un menú
    while True: 
        print('\nMenú de opciones ')
        print('1. Agregar película')
        print('2. Listar películas')
        print('3. Eliminar Catálogo de Películas')
        print('4. Salir')

        opcion=input('Selecciona una opción:')
        if opcion=='1':
            título=input('\nIngresa el título de la película:')
            director=input('\nIngresa el nombre completo del director:')
            año=input('\nIngresa el año de la película:')
            nueva_película= Pelicula(título, director, año) #Se crea una nueva instancia
            catalogo.agregar(nueva_película) #Se agrega al catálogo
            print('\nNueva película agregada')

#creamos unas opciones:
        elif opcion=='2':
            catalogo.listar() #enlista a las películas

        elif opcion=='3':
            catalogo.eliminar() #elimina el catálogo
        
        elif opcion == '4':
            print('\nSaliendo del programa...')
            break #salimos del bucle
        else:
            print('\nOpción no válida')

# Verificamos si el archivo se está ejecutando directamente
if __name__=='__main__': #Llamado a ejecución
    united()
  
