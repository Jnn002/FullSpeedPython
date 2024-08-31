# Funcíon para ingresar valores a una lista, devuelve una lista
def ingreso():
    lista = []
    while True:
        ingreso = input('Ingresa un número: ')
        if ingreso == '':
            break
        lista.append(int(ingreso))
    return lista
    
# Pasamos a nuestro generador la lista creada en la función anterior
def pares(lista):
    for num in lista:
        if num % 2 == 0:
            yield num

# Llamamos a la función y pasamos los valores a una variable
entrada = pares(ingreso())

# Imprimimos los valores pares
for item in entrada:
    print(item)