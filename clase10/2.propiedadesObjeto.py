# 2. Propiedades de un Objeto

# Definir la clase persona:
class Persona:
    def __init__(self, nombre, edad):
        # inicializar las propiedades del objeto
        self.nombre = nombre # propiedad nombre
        self.edad = edad # propiedad edad

# Crear un objeto de la clase persona
persona1 = Persona("Ana", 30)

#Acceder a las propiedades del objeto
print(persona1.nombre)
print(persona1.edad)

# La clase persona define un objeto que tiene propiedades como nombre y edad.
# Al instaciar persona1 con valores especificos, se crean atributos unicos que representan
# el estado de ese objeto.
# Se puede acceder a estas propiedades utilizando la notacion de punto, lo que permite
# obtener informacion sobre la instancia creada.