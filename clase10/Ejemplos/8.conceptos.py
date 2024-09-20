class Animal:  # Superclase
    def hacer_sonido(self):
        return "Sonido de animal"

class Perro(Animal):  # Subclase
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):  # Subclase
    def hacer_sonido(self):
        return "Miau"
