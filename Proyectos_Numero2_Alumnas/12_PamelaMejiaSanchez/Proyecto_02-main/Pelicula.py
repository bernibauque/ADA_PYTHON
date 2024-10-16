#Implementación de la clase Pelicula
# Esta clase se encargará de representar una
# película con sus atributos, como el título*, director* y año de estreno*

class Pelicula:
    def __init__(self, título, director, año):
        self.__título=título  #Atributo título
        self.__director=director #Atributo director
        self.__año=año  #Atributo año

#Notas: Atributos privados y 
#definir un método para acceder al nombre de la película (getter).
    @property
    def título(self): #Getter para título
        return self.__título
    
    @property
    def director (self): #Getter para director
        return self.__director
    
    @property
    def año(self):
        return self.__año #Getter para año

    #Método para que se vea la información de la película en linea o cadena   
    def __str__(self):
        return f'{self.título}, dirigida por {self.director}, año {self.año}'
    
    
    



