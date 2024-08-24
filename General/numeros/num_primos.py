#calcular números primos de 1 a número ingresado

# Crea función para verificar si es primo
def es_primo(num):
    for i in range(2, num-1):
        if num % 2 == 0: return False
    return True

def primos_range(num):
    primos = []
    # Definimos rango que mostraremos, en este caso se mostrará 1 hasta
    # el valor que ingresemos +1 para tomar en cuenta nuestro ingreso
    for i in range (1, num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    # Devolvemos la lista
    return primos

resultado = primos_range(int(input('Ingrese un número para el rango: ')))
print(resultado)
        