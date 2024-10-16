class Pelicula: #Creación de clase película 
    def __init__(self, nombre, director, año, genero):
        self.__nombre = nombre  # Atributo privado
        self.director = director
        self.año = año
        self.genero = genero

    # Getter para nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para nombre
    def set_nombre(self, nombre):
        if nombre: 
            self.__nombre = nombre
        else: 
            print("El nombre de la película no puede estar vacío")

    # Getter para director
    def getdirector(self):
        return self.director

    # Setter para director
    def setdirector(self, director):
        if director:
            self.director = director
        else:
            print("El director no puede estar vacío")

    # Getter para año
    def getaño(self):
        return self.año

    # Setter para año
    def setaño(self, año):
        if isinstance(año, int) and año > 0:
            self.año = año
        else:
            print("El año debe ser un número positivo")

    # Getter para género
    def getgenero(self):
        return self.genero

    # Setter para género
    def setgenero(self, genero):
        if genero:
            self.genero = genero
        else:
            print("El género no puede estar vacío")