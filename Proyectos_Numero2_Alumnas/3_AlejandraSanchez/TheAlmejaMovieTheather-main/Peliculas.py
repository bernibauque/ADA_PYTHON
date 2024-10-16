#Este archivo no posee comentarios que explique cada uno de las funciones y métodos empleados
#En este archivo se encuentra contenida la lógica que permite correr el programa para que el usuario pueda buscar, añadir, enlistar o eliminar películas 
from pelicula import Pelicula
import os

ruta_del_catalogo = r"C:\Users\Santiago Felippelli\Desktop\Proyectos_Numero2_Python\3_AlejandraSanchez\TheAlmejaMovieTheather-main\Catalogo.txt"

def greeting_menu():
    print("Bienvenido a 👑 The Almeja Movie Theater 🎬")
    print("🛑 Este es un programa básico, así que te recomendamos escribir el nombre de tu película sin usar tildes o comillas\n")
    print("Dinos, ¿qué desea hacer?: \n")
    print("1. Buscar una película\n")
    print("2. Agregar una película al catálogo\n")
    print("3. Organizar todas las películas\n")
    print("4. Eliminar el catálogo y crear uno nuevo\n")
    print("5. Salir")

def buscar_pelicula():
    nombre_de_pelicula = input("Escribe la película que quieres buscar en el catálogo: ").strip().lower()
    with open(ruta_del_catalogo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  
            if linea == "":  
                continue
            partes = linea.split(',')
            if len(partes) == 2:  
                nombre, genero = partes
                nombre = nombre.strip().lower() 
                if nombre == nombre_de_pelicula: 
                    print(f"🟢Hemos encontrado la película 📽️ {nombre.title()} en el 📖 catálogo y el género es: {genero}")
                    return
    print("🥺😔 No hemos encontrado la película en el catálogo")

def agregar_pelicula():
    nombre = input("Dinos el nombre de la película que quieres agregar: ")
    genero = input("Ingresa el género de la película que escribiste: ")
    pelicula_agregada = Pelicula(nombre, genero)
    
    with open(ruta_del_catalogo, 'a') as archivo:
        archivo.write(f"{pelicula_agregada.obtener_nombre()},{pelicula_agregada.genero}\n")
    print("Has agregado una nueva película al catálogo")

def organizar_pelicula():
    with open(ruta_del_catalogo, 'r') as archivo:
        peliculas = archivo.readlines()
        
    peliculas.sort()

    with open(ruta_del_catalogo, 'w') as archivo:
        archivo.writelines(peliculas) 
    
    print("Has organizado la lista de películas")

def eliminar():
    if os.path.exists(ruta_del_catalogo):
        os.remove(ruta_del_catalogo)
        print("Has eliminado el catálogo")
        print("Espero que no te arrepientas de esta decisión")
    else:
        print("Es probable que alguien ya haya eliminado el catálogo de pelis, así que debes crear uno desde cero")

opcio_user = ""
while opcio_user != "5":
    greeting_menu()
    opcio_user = input("Escribe el número de la opción que quieres ejecutar para continuar con el programa: ")
    
    if opcio_user == "1":
        buscar_pelicula()
    elif opcio_user == "2":
        agregar_pelicula()
    elif opcio_user == "3":
        organizar_pelicula()
    elif opcio_user == "4":
        eliminar()
    elif opcio_user == "5":
        print("Has salido de tu cinemateca favorita, nos vemos en otra oportunidad 👋")
    else:
        print("⚠️ Tu opción no está en el menú. Por favor, elige una de las opciones indicadas anteriormente")
