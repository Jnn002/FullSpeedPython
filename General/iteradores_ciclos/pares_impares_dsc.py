# Ordenar una lista de númoeros
# definir si son pares e impares y ordenarlos de
# manera descendente 

# ingreso de valores
def ingresoNumeros():
    lista = []
    # Creación de nuestro ciclo while para entrada de datos
    while True:
        ingreso = input("Ingrese un número: ")
        if ingreso == '':
            break
        lista.append(int(ingreso))
    return lista
    
# definir si son pares o impares
def separador(datos):
    # Definición de listas para nuestros números
    pares = []
    impares = []
    # Ciclo para separar los números pares e impares
    for x in datos:
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)
    # Métodos de listas para ordenar de manera descendente
    pares.sort(reverse = True)
    impares.sort(reverse = True)
    return pares, impares

# llamado de funciones
datos = ingresoNumeros()
pares, impares = separador(datos)

# impresión de resultados
print(f'Los números pares son: {pares} y los impares son: {impares}')


