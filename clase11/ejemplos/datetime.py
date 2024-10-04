import datetime

# Fecha actual
fecha_actual = datetime.date.today()
print(f"Fecha actual: {fecha_actual}")

# Hora actual
hora_actual = datetime.datetime.now().time()
print(f"Hora actual: {hora_actual}")

# Fecha y hora actuales
fecha_hora_actual = datetime.datetime.now()
print(f"Fecha y hora actuales: {fecha_hora_actual}")

# Crear una fecha y una hora específicas
mi_fecha = datetime.date(2024, 9, 24)
mi_hora = datetime.time(14, 30, 0)
print(f"Fecha específica: {mi_fecha}")
print(f"Hora específica: {mi_hora}")

# Formatear la fecha actual como 'Día-Mes-Año'
formato_personalizado = fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")
print(f"Fecha y hora formateada: {formato_personalizado}")

# Cálculos con fechas: sumar 10 días a la fecha actual
diferencia = datetime.timedelta(days=10)
nueva_fecha = fecha_actual + diferencia
print(f"Fecha después de 10 días: {nueva_fecha}")

