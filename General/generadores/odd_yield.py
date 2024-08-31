# Devolviendo los números impares con yield()

# Usos de Yield en pytnon y generadores
def impar(n):
    for val in range(n + 1):
        if val % 2 != 0:
            # Devuelve el valor impar
            yield val
            
# Llamamos a la función
mostrar = impar(10)

# Impresión de nuestros valores, con un ciclo for
for item in mostrar:
    print(item)