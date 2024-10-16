# pelicula.py
#Equipo: Elsie Vanessa Ensaldo Renteria & Marcela Kristel Ensaldo Renteria

class Pelicula:
    def __init__(self, nombre):
        # El atributo privado se define con doble guion bajo
        self.__nombre = nombre

    # Método para obtener el nombre de la película
    def obtener_nombre(self):
        return self.__nombre

    # Método para cambiar el nombre de la película
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
