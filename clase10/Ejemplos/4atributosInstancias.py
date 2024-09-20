# 4. Atributos de Instancias

# Definimos la clase Coche
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

# Crear diferentes objetos (instancias) de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

# Acceder a los atributos de instancia
print(coche1.marca)  # Imprime: Toyota
print(coche2.marca)  # Imprime: Honda
