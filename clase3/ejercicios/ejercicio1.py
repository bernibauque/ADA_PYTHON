# Lista de compras vacía
lista_compras = []

while True:
    # Pedir al usuario que ingrese un artículo
    articulo = input("Ingrese un artículo para la lista de compras (o 'done' para finalizar): ")
    
    # Verificar si el usuario ha terminado
    if articulo.lower() == 'done':
        break
    
    # Agregar el artículo a la lista
    lista_compras.append(articulo)
    
    # Preguntar si desea eliminar el último artículo añadido
    eliminar = input("¿Desea eliminar el último artículo añadido? (s/n): ")
    
    if eliminar.lower() == 's':
        lista_compras.pop()
        print("El último artículo ha sido eliminado.")
    else:
        print("Artículo agregado a la lista.")

# Mostrar la lista final de compras
print("Lista de compras final:", lista_compras)

