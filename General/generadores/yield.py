# Usos de Yield en pytnon y generadores
def rango(a, b):
    while a <= b:
        yield a
        a += 1
a = rango(1, 10)

for valor in a:
    print(valor)