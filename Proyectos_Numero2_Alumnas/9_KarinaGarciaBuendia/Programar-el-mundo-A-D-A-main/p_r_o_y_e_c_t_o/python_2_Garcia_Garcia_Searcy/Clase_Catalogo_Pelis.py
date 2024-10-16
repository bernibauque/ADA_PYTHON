import os
from clase_peliculas import Pelicula

class CatalogoPeliculas:
    def __init__(self, ruta_directorio):
        self.nombre_catalogo    =   ''
        self.ruta_directorio    =   ruta_directorio
        self.peliculas          =   []

    def solicitar_nombre_catalogo(self):
        self.nombre_catalogo = input('Escribe el nombre del catálogo: ')
        ruta_catalogo = os.path.join(self.ruta_directorio, self.nombre_catalogo + '.txt')
        if os.path.exists(ruta_catalogo):  
            print('El catálogo ya existe.\n')
        else:
            print(f'Se creo el catálogo {self.nombre_catalogo}.\n')

    def mostrar_menu_catalogo(self):
        print('1. Crear catálogo\n')
        print('2. Lista de catálogos\n')
        print('3. Eliminar catálogo\n')
        print('4. Salir del menú\n')
        elegir_opcion = input('Ingresa un número de las opciones: ')
        return elegir_opcion

    def ejecutar_menu_catalogo(self):

        while True:
            elegir_opcion = self.mostrar_menu_catalogo()
            if not elegir_opcion.isdigit() or int(elegir_opcion) not in range(1, 5):
                print('Opción inválida, intenta de nuevo.')
            else:
                elegir_opcion = int(elegir_opcion)

                if elegir_opcion == 1:
                    print('Escogiste crear un catálogo\n')
                    self.solicitar_nombre_catalogo()
                    self.crear_catalogo()
                    
                elif elegir_opcion == 2:
                    print('Escogiste abrir un catálogo\n')
                    self.mostrar_archivos_txt()
                    self.elegir_catalogo()
                    self.ejecutar_menu_peliculas()
                  
                elif elegir_opcion == 3:
                    print('Escogiste eliminar un catálogo\n')
                    mensaje = self.eliminar_catalogo()
                    print(mensaje)

                elif elegir_opcion == 4:
                    print('Saliendo del menú...')
                    break

# Menú peliculas
    def mostrar_menu_peliculas(self):
        elegir_opcion_pelicula = None
        print(' 1. Lista de películas\n')
        print(' 2. Agregar películas\n')
        print(' 3. Buscar película\n')
        print(' 4. Salir del menú\n')
        elegir_opcion_pelicula = input('Ingresa el número de la opción que quieres ejecutar: ')
        return elegir_opcion_pelicula


    def ejecutar_menu_peliculas(self):
        while True:
            elegir_opcion_pelicula = self.mostrar_menu_peliculas()
            if not elegir_opcion_pelicula.isdigit() or int(elegir_opcion_pelicula) not in range(1,5):
                print('Opción inválida, intenta de nuevamente.')
            else:
                elegir_opcion_pelicula = int(elegir_opcion_pelicula)

                if elegir_opcion_pelicula == 1:
                    print('La siguiente es la lista de películas:\n')
                    self.listar_peliculas()

                elif elegir_opcion_pelicula == 2:
                    print('Agrega una película\n')
                    self.agregar_pelicula()
               

                elif elegir_opcion_pelicula == 3:
                    print('Buscar película\n')
                    self.buscar_pelicula()

                elif elegir_opcion_pelicula ==  4:
                    print('Saliendo del menú de películas...')
                    break

    def agregar_pelicula(self):
        try:
            ruta_archivo = os.path.join(self.ruta_directorio, self.nombre_catalogo + '.txt')
            with open(ruta_archivo, 'a') as archivo:
                titulo      =   input('Título de la película:\n ')
                director    =   input('Director de la película:\n ')
                anio        =   input('Año de la película:\n ')
                genero      =   input('Género de la película:\n ')
                pelicula    =   Pelicula(titulo, anio, genero, director)
                self.peliculas.append(pelicula)
                archivo.write(f'("{titulo}", "{anio}", "{genero}", "{director}")' + '\n')
                print('Película agregada con éxito.')
                self.mostrar_info_pelicula(pelicula)
        except Exception as e:
            print(f'Error al agregar la película: {e}')

    def crear_catalogo(self):
        try:
            ruta_archivo = os.path.join(self.ruta_directorio, self.nombre_catalogo + '.txt')
            with open(ruta_archivo, 'a') as nuevo:
                
                while True:
                    preguntar   =     input('¿Quieres registrar una película en el nuevo catálogo? (S/N) ')
                    if preguntar.lower() != 's':
                        break
                    titulo      =   input('Título de la pélicula:\n ')
                    director    =   input('Director de la película:\n ')
                    anio        =   input('Año de la película:\n ')
                    genero      =   input('Género de la película:\n')
                    pelicula    =   Pelicula(titulo, anio, genero, director)
                    self.peliculas.append(pelicula)
                    nuevo.write(f'("{titulo}", "{anio}", "{genero}", "{director}")' + '\n'+ '\n')
                    continuar   =   input('¿Deseas añadir otra película? (S/N):\n ')
                    if continuar.lower() != 's':
                        break
                print('Catálogo creado con éxito')
        except Exception as e:
            print(f'Error al crear el catálogo: {e}')


    def mostrar_archivos_txt(self):
        try:
            archivos_catalogos      =   os.listdir(self.ruta_directorio)
            archivos_catalogos_txt  =   [archivo for archivo in archivos_catalogos if archivo.endswith('.txt')]
            if archivos_catalogos_txt:
                print('Los catálogos son:\n ')
                for i, archivo in enumerate(archivos_catalogos_txt, 1):
                    print(f'{i}. {archivo}')
            else:
                print('No se encontró ningún catálogo en el directorio.')
        except Exception as e:
            print(f'Error al listar los catálogos: {e}')
    
    def elegir_catalogo(self):
        archivos_catalogos      =   os.listdir(self.ruta_directorio)
        archivos_catalogos_txt  =   [archivo for archivo in archivos_catalogos if archivo.endswith('.txt')]
        elegir_archivo = input('Ingresa el número del catálogo que deseas abrir: ')

        if elegir_archivo.isdigit() and 1 <= int(elegir_archivo) <= len(archivos_catalogos_txt):
            self.nombre_catalogo = archivos_catalogos_txt[int(elegir_archivo) - 1].replace('.txt', '')
            print(f'Seleccionaste el catálogo: {self.nombre_catalogo}\n')
        else:
            print('Número de catálogo inválido.')

    def listar_peliculas(self):
        ruta_archivo = os.path.join(self.ruta_directorio, self.nombre_catalogo + '.txt')
        try:
            with open(ruta_archivo, 'r') as archivo:
                    print('Las películas en el catálogo son:\n ')
                    for numero, linea in enumerate(archivo, start=1):
                        print(f'{numero}. {linea.strip()}')   
        except Exception as e:
            print(f'Error al listar las películas del catálogo: {e}.')

                        
    def eliminar_catalogo(self):
        try:
            archivos_catalogos      =   os.listdir(self.ruta_directorio)
            archivos_catalogos_txt  =   [archivo for archivo in archivos_catalogos if archivo.endswith('.txt')]
            if archivos_catalogos_txt:
                print('Los catalogós que puedes eliminar son:\n ')

                for i, archivo in enumerate(archivos_catalogos_txt, 1):
                    print(f'{i}. {archivo}')
                elegir_archivo = input('Ingresa el número del archivo que deseas eliminar: ')

                if elegir_archivo.isdigit() and 1 <= int(elegir_archivo) <= len(archivos_catalogos_txt):
                    archivo_a_eliminar = archivos_catalogos_txt[int(elegir_archivo) - 1]
                    ruta_archivo = os.path.join(self.ruta_directorio, archivo_a_eliminar)
                    os.remove(ruta_archivo)
                    print(f'El archivo {archivo_a_eliminar} fue eliminado.')
            else:
                print('No hay catálogos en el directorio.')
        except Exception as e:
            print(f'Error al eliminar el catálogo en el directorio: {e}')

# Método para mostrar información
    def mostrar_info_pelicula(self, pelicula):
            print(f'Nombre de la película es {pelicula.titulo} y el género es {pelicula.genero}.\n')
            print(f'El director de {pelicula.titulo} es {pelicula.director} y se estrenó en el año {pelicula.anio}\n')  # Imprime la información

    def buscar_pelicula(self):
        ruta_archivo = os.path.join(self.ruta_directorio, self.nombre_catalogo + '.txt')
        titulo_a_buscar = input('Ingresa el título de la película que deseas buscar: ')
        try:
            with open(ruta_archivo, 'r') as archivo:
                peliculas    =  archivo.readlines()
                encontrado   =  False
                for pelicula in peliculas:
                    if titulo_a_buscar.lower() in pelicula.lower():
                        print(pelicula)
                        encontrado = True
                if not encontrado:
                    print('Película no encontrada.')
        except Exception as e:
            print(f'Error al buscar la película: {e}')              

# Crear una instancia y ejecutar el menú
ruta_directorio = r'C:\Users\Santiago Felippelli\Desktop\Proyectos_Numero2_Python\9_KarinaGarciaBuendia\Programar-el-mundo-A-D-A-main\p_r_o_y_e_c_t_o\python_2_Garcia_Garcia_Searcy'
catalogo        = CatalogoPeliculas(ruta_directorio)
catalogo.ejecutar_menu_catalogo()
catalogo.ejecutar_menu_peliculas()
