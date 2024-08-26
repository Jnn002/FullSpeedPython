# Verificar si existen valores repetidos en una lista
def verificarRepetidos(lista):
    for x in lista:
        # Si el valor se repite más de una vez, retornar True
        if lista.count(x) > 1:
            return True
    # Si no se repite, retornar False
    return False

def ingresolista():
    lista = []
    while True:
        ingreso = input("Ingrese un número: ")
        if ingreso == '' or ingreso == 'q':
            break
        lista.append(int(ingreso))
    return lista

print(verificarRepetidos(ingresolista()))