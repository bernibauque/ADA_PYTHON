class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de Animal
        self.raza = raza

mi_perro = Perro("Rex", "Labrador")
print(mi_perro.nombre)  # Imprime: Rex
print(mi_perro.raza)    # Imprime: Labrador
