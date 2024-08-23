# Otra forma de hacerlo es con list comprehens
def listaParesImpares(num):
    pares = []
    impares = []
    pares = [x for x in range(1, num) if x % 2 == 0]
    impares = [x for x in range(1, num) if x % 2 != 0]
    return [pares, impares]
print(f'Las listas de pares e impares son:\n{listaParesImpares(int(input("Ingrese un número para el rango: ")))}')