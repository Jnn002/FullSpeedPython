# Ingresar texto a un archivo de texto
ingreso = []

# Ciclo para ingreso de texto
while True:
    linea = input('Escribe algo para agregarlo: ')
    if linea == '':
        break
    ingreso.append(linea + '\n')

# Permiso para agregar al archivo de texto, sin sobreescribir => 'a'
with open('Data_types/texto/archivo.txt', 'a') as archivo:
    archivo.writelines(ingreso)