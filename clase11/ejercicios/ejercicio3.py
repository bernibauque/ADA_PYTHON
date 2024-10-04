from datetime import datetime

# Solicitar la fecha de nacimiento
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")

# Convertir la cadena de texto a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")

# Calcular la edad
fecha_actual = datetime.now()
edad = fecha_actual.year - fecha_nacimiento.year

# Ajustar la edad si aún no ha cumplido años este año
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

print(f"Tienes {edad} años.")

# Mostrar la fecha actual en diferentes formatos
print(f"\nFecha actual en diferentes formatos:")
print(f"Día-Mes-Año: {fecha_actual.strftime('%d-%m-%Y')}")
print(f"Mes/Día/Año: {fecha_actual.strftime('%m/%d/%Y')}")
print(f"Año/Mes/Día: {fecha_actual.strftime('%Y/%m/%d')}")
