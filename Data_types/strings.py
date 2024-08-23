# Análisis, validar palinndromo

while True:
    # SOlicitamos nuestra palabra, la pasamos a minúsculas y eliminamos los espacios
    palabra = input("Ingrese una palabra: ").lower().strip()
    # Invertimos el orden de nuestra palabra 
    palabra_inversa = palabra[::-1]
    # Salimos del bucle de ejecución si la palabra es vacía
    if palabra == '':
        break 
    # Comparación de nuestras cadena y mostramos el resultado 
    if palabra != palabra_inversa:
        print('Esta palabra no es un palíndromo')
    else:
        print('Esta palabra es un palíndromo')
    continue