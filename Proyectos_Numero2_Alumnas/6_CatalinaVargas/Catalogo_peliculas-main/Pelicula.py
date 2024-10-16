# Archivo

class pelicula:
    def __init__(self, nombre):
        self.__nombre_pelicula = nombre #Atributo privado
        
        """ Comentario Cata: 
        Usar __init__ nos sirve para guardar el nombre de la clase, es decir el nombre de la peli y lo asigna a un atributo privado 
        __ esto se usa para que el atriburo no pueda ser modificado directamente desde la clase.
        Importante para recordar: la clase es como la receta, es una guía. 
        Los objetos son cosas que tienen características, en este caso la caraterística es el nombre (atributo)
        Los métodos son lo que puede hacer
        Un constructor es una función que se ejecuta automáticamente cuando creas el objeto (pelicula); el constructor define características de tu película, como por ejempl
        el nombre."""
        
    def pelicula_nombre(self):
        """ Al usar "pelicula_nombre, nos permite ver el nombre de la película aunque sea privado."""
        
        return self.__nombre_pelicula
    
        