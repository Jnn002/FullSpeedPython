# import de liberia math
import math as m
def trigoFun(x):
    seno = m.sin(x)
    coseno = m.cos(x)
    tangente = m.tan(x)
    return [seno, coseno, tangente]

valor = trigoFun(int(input('Valor de X: ')))
print(valor)