# Eliminar elementos de una lista según valores de otra
def removerValores():
    # Definicion de nuestras listas
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [3, 4, 5]
    # Ciclo en el que iteramos hasta que la lista2 este vacia
    for x in lista2:
        lista1.remove(x)
    return lista1
# Llamamos a la funcion y guardamos el resultado en una variable
nueva_lista = removerValores()
print(nueva_lista)