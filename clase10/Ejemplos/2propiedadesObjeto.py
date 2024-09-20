# 2. Propiedades de un Objeto

# Definimos la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        # Inicializamos las propiedades del objeto
        self.nombre = nombre  # Propiedad: nombre
        self.edad = edad      # Propiedad: edad

# Crear un objeto de la clase Persona
persona1 = Persona("Ana", 30)

# Acceder a las propiedades del objeto
print(persona1.nombre)  # Imprime: Ana
print(persona1.edad)    # Imprime: 30
