# Números pares dado un rango, elevados al cuadrado y luego sumados
def cuadrados():
    #lsita 0 al 21
    lista = [x*x for x in range(0,21) if x % 2 == 0]
    sumatoria = sum(lista)
    return sumatoria

resultado = cuadrados()
print(resultado)