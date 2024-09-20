# 6. Métodos de Clase

# Definimos la clase Coche
class Coche:
    cantidad_de_coches = 0  # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia
        Coche.cantidad_de_coches += 1  # Aumenta la cantidad total de coches

    # Método de clase para obtener el total de coches
    @classmethod
    def total_coches(cls):
        return f"Total de coches: {cls.cantidad_de_coches}"

# Crear instancias de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

# Llamar al método de clase
print(Coche.total_coches())  # Imprime: Total de coches: 2
