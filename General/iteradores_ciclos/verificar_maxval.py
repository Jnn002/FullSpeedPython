# Verificar con un loop el valor más alto, simple loop
""" valores = [10, 20, 30, 40, 50]
    paso = 0
    for x in valores:
        if x > paso:
            paso = x
    print(paso) """
    
# Verificar con un loop el valor más alto, loop con funciones
# y una función de entrada de datos, además de una función de búsqueda
# que nos devuelve el indice del valor más alto
def buscarMaxValue(lista):
    paso = lista[0]
    index = 0
    for x in range(1, len(lista)):
        if lista[x] > paso:
            paso = lista[x]
            index = x
    return [paso, index]

def entrada():
    lista = []
    while True:
        agregar = input("Ingrese un número: ")
        if agregar == '' or agregar == 'q':
            break
        lista.append(int(agregar))
    return lista

mostrar, indice = buscarMaxValue(entrada())
print(f'El valor más alto es: {mostrar} y {indice}')

