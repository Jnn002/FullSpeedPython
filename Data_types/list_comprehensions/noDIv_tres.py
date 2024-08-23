# Números pares dado un rango, elevados al cuadrado y luego sumados, 
# pero que no sean divisibles por 3
def cuadrados():
    # Utilizamos operador 'and' para agregar una condición adicional
    lista = [x*x for x in range(0,21) if x % 2 == 0 and x % 3 != 0]
    sumatoria = sum(lista)
    return sumatoria

resultado = cuadrados()
print(resultado)