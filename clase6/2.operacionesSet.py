# Crear conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
conjunto_c = {7, 8, 9}

# Subconjunto
es_subconjunto = conjunto_a.issubset(conjunto_b)
print(f"Es conjunto_a un subconjunto de conjunto_b: {es_subconjunto}")

# SuperConjunto
es_superconjunto = conjunto_b.issuperset(conjunto_a)
print(f"Es conjunto_b un superconjunto de conjunto_a?: {es_superconjunto}")

# Disconjuntoos
son_disconjuntos = conjunto_a.isdisjoint(conjunto_c)
print(f"Son conjunto_a y conjunto_c disjuntos?: {son_disconjuntos}")

#Simetria 
simetria = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simetrica entre conjunto_a y conjunto_b: {simetria}")

#Union Update 
conjunto_a.update(conjunto_b)
print(f"Conjunto_a despues de la union con conjunto_b: {conjunto_a}")

#Interseccion Update
conjunto_a.intersection_update(conjunto_b)
print(f"Conjunto_a despues de la interseccion con conjunto_b: {conjunto_a}")

#Difference Update
conjunto_a.difference_update(conjunto_b)
print(f"Conjunto_b despues de la diferencia con conjunto_c: {conjunto_a} ")

#Symmetric Difference Update
conjunto_a.symmetric_difference_update(conjunto_b)
print(f"Conjunto_a despues de la diferencia simetrica con conjunto_b: {conjunto_b}")




