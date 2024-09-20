# Lista de alumnos y sus calificaciones
alumnos = ['Ana', 'Juan', 'María', 'Luis', 'Carmen']
calificaciones = [85, 55, 90, 40, 70]

# Listas vacías para aprobados y desaprobados
aprobados = []
desaprobados = []

# Recorre las calificaciones y clasifica a los alumnos
for i in range(len(calificaciones)):
    if calificaciones[i] >= 60:
        aprobados.append(alumnos[i])
    else:
        desaprobados.append(alumnos[i])

# Mostrar las listas de aprobados y desaprobados
print("Aprobados:", aprobados)
print("Desaprobados:", desaprobados)
