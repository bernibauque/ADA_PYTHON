# Importando el módulo completo
import clase11.ejemplos.operaciones as operaciones

print(f"Suma (import completo): {operaciones.sumar(2, 3)}")

# Renombrando el módulo
import clase11.ejemplos.operaciones as op

print(f"Resta (modulo renombrado): {op.restar(5, 2)}")

# Importando una función específica
from clase11.ejemplos.operaciones import multiplicar

print(f"Multiplicación (función específica): {multiplicar(3, 4)}")

# Renombrando una función específica
from clase11.ejemplos.operaciones import sumar as suma

print(f"Suma (función renombrada): {suma(10, 20)}")

# Importando todo el módulo con *
from clase11.ejemplos.operaciones import *

print(f"Resta (import *): {restar(10, 4)}")
