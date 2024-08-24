# Verificar si un número es divisible entre otro
def esDivisible(a, b):
    if a % b == 0:
        return True
    else:
        return False
    
print(esDivisible(int(input('Ingrese el primer número: ')), int(input('Ingrese el segundo número: '))))