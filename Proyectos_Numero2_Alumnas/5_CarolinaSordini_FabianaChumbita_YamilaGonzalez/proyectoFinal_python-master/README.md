
alumnas: Carolina Sordini, Yamila Julia González, Fabiana Andrea chumbita.

Catalogo de Peliculas

-------PELICULA.PY-------

En este proyecto empezamos creando dos clases:

La primera llamada Pelicula: Utilizamos el método constructor de la clase, que llama automáticamente cuando se crea una nueva instancia de Pelicula, toma un parámetro "nombre", representando al nombre de la Pelicula.
Asignamos el valor del parámetro nombre a un atributo de instancia llamado __nombre. Usamos doble guion bajo para indicar que se trara de un atributo privado, no se puede acceder directamente desde afuera de la clase, es una forma de encapsulacion que ayuda a protejer los datos. Por otro lado asignamos el metodo obtener_nombre que permite acceder al nombre de la película de manera controlada.

La segunda llamada catalogo_peliculas: está diseñada para gestionar un catálogo de películas. Permite agregar, listar y vacias peliculas. Utiliza un archivo JSON para almacenar la información de las películas de forma persistente.
Consta de 2 atributos, una es nombre, almacena el nombre del catálogo. Y la otra ruta_archivo, define la ubicación del archivo JSON donde se guardarán los datos del catálogo.

-------CATALOGO_PELICULAS.PY----------

Explicacion de como funciona:
1 - El método agregar permite añadir una película al catálogo de manera segura, manejando errores potenciales y actualizando un archivo JSON que almacena la lista de películas. Si se produce un error en cualquier parte del proceso, se informará al usuario sin interrumpir el funcionamiento del programa.
El usuario debe ingresar la opción 1 y automáticamente el código pedirá ingresar el nombre de la película que se quiere agregar, luego debe dar enter y la película agregada se incorporará en el archivo JSON. 
2 - El método listar se encarga de mostrar todas las películas del catálogo. Si hay películas, las imprime en un formato enumerado. Si el catálogo está vacío, informa al usuario de esa situación. Además, maneja adecuadamente el caso en que el archivo del catálogo no existe, asegurando que el programa no se interrumpa debido a errores.
En este método el usurario debe ingresar la opción 2 para que las películas del archivo JSON se enumeren, comenzando desde el 1 en adelante. 
3 - El método eliminar se utiliza para vaciar el archivo del catálogo de películas, eliminando todas las entradas. Maneja errores potenciales y proporciona un mensaje informativo al usuario tanto si la operación es exitosa como si ocurre un problema.
A este método se ingresa eligiendo la opción 3, y se podrá observar el vaciamiento de la carpeta de texto JSON. 
4 - Salir: En este punto simplemente ingresando la opción 4 automáticamente se sale del catálogo películas.

El método _cargar_catalogo está diseñado para leer y cargar el catálogo de películas desde un archivo JSON. Maneja situaciones en las que el archivo no existe o no se puede decodificar, devolviendo una lista vacía en tales casos. Esto permite que el resto del programa funcione sin interrupciones, incluso si el catálogo no está disponible.

La función mostrar_menu presenta al usuario las opciones disponibles para interactuar con el catálogo de películas.
La función main gestiona el flujo del programa, creando un catálogo y permitiendo al usuario agregar, listar o vaciar películas, o salir del programa. Utiliza un bucle que se repite hasta que el usuario decide salir.