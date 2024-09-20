# 1. Definir una Clase en Python

# Definimos una clase llamada Coche
class Coche:
    # El método __init__ es el constructor que se llama al crear un nuevo objeto
    def __init__(self, marca, modelo):
        # self es una referencia al objeto que estamos creando
        # Inicializamos los atributos de la instancia
        self.marca = marca  # Atributo de instancia: guarda la marca del coche
        self.modelo = modelo  # Atributo de instancia: guarda el modelo del coche
