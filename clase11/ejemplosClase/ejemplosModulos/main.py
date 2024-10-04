# Importamos el modulo completo
import operaciones
print(f"Suma (import completo): {operaciones.sumar(2, 3)}")

# Renombramos el modulo
import operaciones as op
print(f"Resta (modulo renombrado): {op.restar(5, 2)}")

# Importar una funcion especifica
from operaciones import multiplicar
print(f"Multiplicacion (funcion especifica): {multiplicar(3, 2)}")

# Renombramos una funcion especifica
from operaciones import sumar as suma
print(f"Suma (funcion renombrada): {suma(10, 70)}")

# Importando todo el modulo con *
from operaciones import *
print(f"Resta (import *): {restar(30, 5)}")