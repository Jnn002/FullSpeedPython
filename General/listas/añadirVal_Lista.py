
# Función que añade valores a una lista 
def añadirVal_Lista():
    # Lista inicial
    lista = [1,2,3,4,5]
    # Ciclo para añadir valores a la lista
    while True:
        ingreso = input("Ingrese el valor a añadir a la lista: ")
        if ingreso == '':
            break
        lista.append(ingreso)
    # Retorno de la lista
    return lista

# Llamada a la función
valor = añadirVal_Lista()
print(valor)
