# Paso 1: Definir el nombre del archivo
nombre_archivo = 'archivo.txt'

# Paso 2: Leer todo el contenido de una sola vez usando read()
# Abre el archivo en modo de lectura ('r') y lo asigna a la variable 'archivo'.
# Usamos 'with', para que el archivo se cierre automáticamente cuando 
# se termine el bloque.
with open(nombre_archivo, 'r') as archivo:
    print("Leyendo todo el archivo de una vez con read():")
    # Utiliza el método read() para leer todo el contenido del archivo de una sola vez.
    contenido_completo = archivo.read()
    print(contenido_completo)
    #línea de separación (40 guiones) para distinguir las diferentes lecturas.
    print("-" * 40)

# Paso 3: Leer el archivo línea por línea usando readline()
with open(nombre_archivo, 'r') as archivo:
    print("Leyendo el archivo línea por línea con readline():")
    # Usa el método readline() para leer la primera línea del archivo.
    linea = archivo.readline()
    # Mientras la variable 'linea' contenga contenido (no esté vacía), sigue leyendo.
    while linea:
        # Imprime la línea, pero usa strip() para eliminar los saltos de línea al final de cada línea leída.
        print(linea.strip())
        # Lee la siguiente línea del archivo. Si no hay más líneas, 
        # readline() devolverá una cadena vacía, terminando el bucle.
        linea = archivo.readline()
    # Imprime una línea de separación (40 guiones).
    print("-" * 40)

# Paso 4: Leer todas las líneas a la vez usando readlines()
with open(nombre_archivo, 'r') as archivo:
    print("Leyendo todas las líneas de una sola vez con readlines():")
    # Usa el método readlines() para leer todas las líneas del archivo a la vez.
    # El resultado es una lista de cadenas, donde cada cadena es una línea del archivo.
    lineas = archivo.readlines()
    # Se recorre la lista de líneas utilizando un bucle 'for'.
    for linea in lineas:
        # Imprime cada línea después de eliminar los saltos de línea con strip().
        print(linea.strip())
    # Imprime una línea de separación (40 guiones) para finalizar.
    print("-" * 40)

