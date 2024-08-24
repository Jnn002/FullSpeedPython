def sumList(lista):
    lista = []
    while True:
        valor = input("Ingrese un número o 'q' para salir: ")
        if valor == 'q' or valor == '':
            break
        else: 
            lista.append(int(valor))
    return lista

def sumador(numeros):
    numeros = sumList(lista=[])
    return sum(numeros)

# OTRA FORMA DE LLAMAR SUMADOR
""" def sumador(numeros):
        suma = 0
        for x in numeros:
            suma += x
        return suma
        
    numeros = sumList(lista=[])
    print(sumador(numeros)) """
