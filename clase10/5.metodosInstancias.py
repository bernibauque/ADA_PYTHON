# 5. Metodos de instancias

# Definimos la clase
class Perro:
    def __init__(self, raza, nombre):
        self.raza = raza # Atributo de instancia
        self.nombre = nombre # Atributo de instancia

    # Metodo para mostrar informacion del perrito
    def mostrar_info(self):
        return f"Perro: {self.raza} {self.nombre}"
        
# Crear un objeto de la clase perro
mi_perro = Perro("Mestiza", "Canelita")

# Usar el metodo del objeto
print(mi_perro.mostrar_info())

# En la clase perro, el metodo mostrar_info es un metodo de instancia que proporciona
# una representacion de la informacion del perro al acceder a sus atributos.
# Este metodo permite realizar acciones espercificas sobre los datos del objeto, y se invoca
# a traves de la instancia de perro para obtener detalles sobre ese objeto en particular