# Ejemplo 1: Función Básica Anidada
def funcion_externa(x):
    """
    Función externa que recibe un parámetro 'x' y define una función interna.
    
    :param x: Valor entero para el cálculo.
    :return: Resultado de la función interna llamada con 'x'.
    """
    def funcion_interna(y):
        """
        Función interna que recibe un parámetro 'y' y lo suma a 10.
        
        :param y: Valor entero que se suma a 10.
        :return: Valor entero resultante de la suma.
        """
        return y + 10
    
    # Llamada a la función interna con el valor de 'x'
    return funcion_interna(x)

# Llamada a la función externa
resultado = funcion_externa(5)
print(f"Resultado de funcion_externa(5): {resultado}")  # Imprime 15

# Ejemplo 2: Cierre (Closure)
def crear_multiplicador(factor):
    """
    Crea una función que multiplica su entrada por un 'factor' específico.
    
    :param factor: Valor por el que se multiplicarán los argumentos de la función interna.
    :return: Función que multiplica su entrada por el 'factor'.
    """
    def multiplicar(x):
        """
        Función interna que multiplica 'x' por 'factor'.
        
        :param x: Valor entero a multiplicar.
        :return: Resultado de la multiplicación.
        """
        return x * factor
    
    return multiplicar

# Crear dos funciones multiplicadoras con diferentes factores
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

# Usar las funciones multiplicadoras
print(f"Duplicar 10: {duplicar(10)}")  # Imprime 20
print(f"Triplicar 10: {triplicar(10)}")  # Imprime 30

# Ejemplo 3: Función Anidada con Variables Locales
def calcular_area_con_perimetro(base, altura):
    """
    Calcula el área y el perímetro de un rectángulo usando una función anidada.
    
    :param base: Base del rectángulo.
    :param altura: Altura del rectángulo.
    :return: Tupla con el área y el perímetro del rectángulo.
    """
    def calcular_perimetro(base, altura):
        """
        Función interna que calcula el perímetro del rectángulo.
        
        :param base: Base del rectángulo.
        :param altura: Altura del rectángulo.
        :return: Perímetro del rectángulo.
        """
        return 2 * (base + altura)
    
    area = base * altura
    perimetro = calcular_perimetro(base, altura)
    
    return area, perimetro

# Llamada a la función principal
area, perimetro = calcular_area_con_perimetro(5, 3)
print(f"Área: {area}, Perímetro: {perimetro}")  # Imprime "Área: 15, Perímetro: 16"

# Ejemplo 4: Uso de `nonlocal` en Funciones Anidadas
def contador():
    """
    Función que devuelve una función para incrementar un contador.
    
    :return: Función que incrementa el contador y devuelve el valor.
    """
    cuenta = 0
    
    def incrementar():
        """
        Función interna que incrementa la variable 'cuenta'.
        
        :return: Valor incrementado de la variable 'cuenta'.
        """
        nonlocal cuenta
        cuenta += 1
        return cuenta
    
    return incrementar

# Crear una función contador
mi_contador = contador()

# Llamar a la función contador varias veces
print(f"Contador 1: {mi_contador()}")  # Imprime 1
print(f"Contador 2: {mi_contador()}")  # Imprime 2
print(f"Contador 3: {mi_contador()}")  # Imprime 3
