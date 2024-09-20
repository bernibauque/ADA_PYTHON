class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())  # Aquí se aplica el polimorfismo

mi_perro = Perro()
mi_gato = Gato()

hacer_sonido_animal(mi_perro)  # Imprime: Guau
hacer_sonido_animal(mi_gato)    # Imprime: Miau
