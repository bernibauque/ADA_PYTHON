# Crear el diccionario anidado
clubes = {
    'Club A': [
        {'nombre': 'Juan', 'edad': 25},
        {'nombre': 'Pedro', 'edad': 30}
    ],
    'Club B': [
        {'nombre': 'Ana', 'edad': 22},
        {'nombre': 'Luis', 'edad': 28},
        {'nombre': 'María', 'edad': 31}
    ],
    'Club C': [
        {'nombre': 'Carlos', 'edad': 27}
    ]
}

# Contar jugadores en cada club
num_jugadores_club_a = len(clubes['Club A'])
num_jugadores_club_b = len(clubes['Club B'])
num_jugadores_club_c = len(clubes['Club C'])

print("Número de jugadores en Club A:", num_jugadores_club_a)
print("Número de jugadores en Club B:", num_jugadores_club_b)
print("Número de jugadores en Club C:", num_jugadores_club_c)
