# 3. Atributos de Clase

# Definimos la clase Coche
class Coche:
    ruedas = 4  # Atributo de clase: todas las instancias de Coche tienen 4 ruedas

    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

# Imprimir el atributo de clase
print(Coche.ruedas)  # Imprime: 4

# Crear instancias de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

# Acceder al atributo de clase desde las instancias
print(coche1.ruedas)  # Imprime: 4
print(coche2.ruedas)  # Imprime: 4
