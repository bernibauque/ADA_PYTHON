# 4. Atributos de Instacias

# Definimos la clase 
class Gato:
    def __init__(self, color, nombre):
        self.color = color # Atributo instancia
        self.nombre = nombre # Atributo instancia

# Crear diferentes objetos (instancias) de la clase gato
gato1 = Gato("negro", "Felix")
gato2 = Gato("gris", "Ares")

# Acceder a los atributos de instancia
print(gato1.color)
print(gato2.color)

# La clase Gato incluye atributos de instancia, color y nombre, que se inicializan en el constructor.
# Cada objeto creado a partir de esta clase (como gato1 y gato2) tiene sus propios valores para estos atributos
# lo que permite que diferentes instancias representen gatos distintos con caracteristicas unicas.


