# Funcion que recibe un número y retorna listas
# con los números pares e inpares del rango de 0 al número ingresado
def separador(numero):
    # Definición de listas para nuestros números
    pares = []
    inpares = []
    for num in range(numero):
        if num % 2 == 0: 
            pares.append(num)
        else: 
            inpares.append(num)
    return pares, inpares
# Solicitamos un número al usuario, para el rango
pares, inpares = separador(int(input('Ingrese un número para el rango: ')))
# nos devuele la lista de numeros pares e inpares
print(f'La lista de números pares es {pares} y los inpares son {inpares}')
# Contamos la cantidad de números pares e inpares
cuenta_par = len(pares)
cuenta_inpar = len(inpares)
print(f'La cantidad de números pares es {cuenta_par} y de números inpares es {cuenta_inpar}')