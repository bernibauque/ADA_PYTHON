
#  Esta clase se encargará de representar una película con sus atributos, como el nombre.


class Pelicula:
    tipo = 'Cine'                                               # Atributo de clase
    
    def __init__(self, titulo, anio, genero, director):
        self.__titulo   = titulo                               # Atributo de instancia
        self.__anio     = anio
        self.genero     = genero
        self.director   = director

    def __str__(self):
        return f'("{self.titulo}", "{self.anio}", "{self.genero}", "{self.director}")'

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            raise ValueError('El nombre debe ser una cadena de texto')

    @property
    def anio(self):
        return self.__anio
    
    @anio.setter
    def anio(self, corregir_anio):
        if isinstance(corregir_anio, int):
            self.__anio = corregir_anio
        else:
            raise ValueError('El año de la película debe ser un número')

