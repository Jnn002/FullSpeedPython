# # Revisar paridad
def checkParity(n):
    if n % 2 == 0:
        result = 'Par'    
    else:     
        result = 'Impar'
    return result

definicion = checkParity(int(input('Ingresa un número: ')))
print(definicion)