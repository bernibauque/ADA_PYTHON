# Ejemplo: Gestión de asistentes a un evento
# Objetivo: Crear un programa que administre una lista de asistentes 
# a un evento sin permitir duplicados y que realice operaciones 
# entre dos listas de invitados.

# Crear conjuntos de invitados
invitados_viernes = {"Ana", "Carlos", "Pedro", "Luis", "Clara"}
invitados_sabado = {"Carlos", "Luis", "Sofía", "María", "Pedro"}

# Mostrar los invitados únicos que asistieron el viernes
print(f"Invitados del viernes: {invitados_viernes}")

# Mostrar los invitados únicos que asistieron el sábado
print(f"Invitados del sábado: {invitados_sabado}")

# Mostrar la unión (quién asistió al menos un día)
todos_asistentes = invitados_viernes | invitados_sabado
print(f"Asistentes de ambos días: {todos_asistentes}")

# Mostrar la intersección (quién asistió ambos días)
asistieron_ambos_dias = invitados_viernes & invitados_sabado
print(f"Asistieron ambos días: {asistieron_ambos_dias}")

# Mostrar la diferencia (quién asistió solo el viernes)
solo_viernes = invitados_viernes - invitados_sabado
print(f"Asistieron solo el viernes: {solo_viernes}")

# Agregar un nuevo invitado el sábado
invitados_sabado.add("Miguel")
print(f"Invitados del sábado después de agregar a Miguel: {invitados_sabado}")

# Eliminar un invitado que canceló
invitados_sabado.remove("María")
print(f"Invitados del sábado después de eliminar a María: {invitados_sabado}")

# Comprobar si Ana asistió el sábado
print(f"¿Ana asistió el sábado?: {'Ana' in invitados_sabado}")











