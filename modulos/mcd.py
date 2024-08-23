# Importamos la libreria math
import math as m

# Función para calcular maximo común divisor de 2 números
def buscaMCD(a, b):
    return m.gcd(a, b)

resultado = buscaMCD(a = int(input('Primer Número: '))
                    ,b = int(input('Segundo Número: ')))
print(resultado)