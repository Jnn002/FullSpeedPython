def elmayor(a, b):
    if a == b:
        return 'Los números son iguales'
    elif a > b:
        return 'El número mayor es: ' + str(a)
    else:
        return 'El número mayor es: ' + str(b)

entrada = elmayor(int(input('Ingrese el primer número: ')), int(input('Ingrese el segundo número: ')))
print(entrada)
        