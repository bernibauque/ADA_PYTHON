#Escribe un programa que asigna un mensaje a una variable resultado basado en una calificación (entre 0 y 100). 
# Usa el operador ternario para asignar "Aprobado" si la calificación es mayor o igual a 60 y "Reprobado" en caso contrario.

# Solicita la calificación al usuario
calificacion = float(input("Introduce tu calificación: "))

# Usa el operador ternario para determinar el resultado
resultado = "Aprobado" if calificacion >= 60 else "Reprobado"

print(resultado)
