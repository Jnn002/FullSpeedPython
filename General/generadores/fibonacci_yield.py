# GENERADOR QUE NOS DEVUELVE LA 'CANTIDAD' DE NÚMEROS DE LA SERIE DE FIBONACCI QUE LE INDIQUEMOS
def fiboyi(n):
    lista = []
    for i in range(n):
        if i == 0 or i == 1:
            lista.append(i)
            yield i
        else:
            x = lista[i-2] + lista[i-1]
            lista.append(x)
            yield x
            
limite = fiboyi(int(input('Ingrese la cantidad de valores de la serie \nde Fibonacci que desea conocer: ')))

for item in limite:
    print(item)