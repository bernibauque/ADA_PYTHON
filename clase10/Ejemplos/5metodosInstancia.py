# 5. Métodos de Instancias

# Definimos la clase Coche
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

    # Método para mostrar información del coche
    def mostrar_info(self):
        return f"Coche: {self.marca} {self.modelo}"

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")

# Usar el método del objeto
print(mi_coche.mostrar_info())  # Imprime: Coche: Toyota Corolla
