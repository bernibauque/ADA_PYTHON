# Gestion de asistentes a un evento
# Crear un programa que administre una lista de 
# asistentes a eventos sin permitir duplicados 
# y que realice operaciones entre dos listas

# Crear conjuntos de invitados
invitados_viernes = {"Ana", "Carlos", "Pedro", "Luis", "Clara"}
invitados_sabado = {"Carlos", "Luis", "Sofia", "Maria", "Pedro"}

# Mostrar a los invitados unicos que asisten el viernes
print(f"Invitados de viernes: {invitados_viernes}")

# Mostrar a los invitados unicos que asisten el sabado
print(f"Invitados de sabado: {invitados_sabado}")

# Mostrar la union (quien asistio ambos dias)
todos_asistentes = invitados_sabado | invitados_viernes
print(f"Asistentes de ambos dias: {todos_asistentes}")

# Mostrar la interseccion (quien asistio al menos un dia)
solo_viernes = invitados_viernes & invitados_sabado
print(f"Asistentes solo el viernes: {solo_viernes}")

# Mostrar la diferencia 
solo_viernes = invitados_viernes -invitados_sabado
print(f"Asistencia solo el viernes: {solo_viernes}")

# Agregar un nuevo invitado el sabado
invitados_sabado.add("Miguel")
print(f"Invitados del sabado despues de agregar un nuevo invitado: {invitados_sabado}")

# Eliminar un invitado que cancelo
invitados_sabado.remove("Maria")
print(f"Invitados del sabado despues de eliminar un invitado: {invitados_sabado}")

# Comprobar si Ana asistio el sabado
print(f"Ana asistio el sabado?: {'Ana' in invitados_sabado}")