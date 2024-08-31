def impares(n):
    for val in range(n,-1, -1):
        if val % 2 != 0:
            yield val
            
valores = impares(int(input('Ingresa el limite superior del rango: ')))
for item in valores:
    print(item)