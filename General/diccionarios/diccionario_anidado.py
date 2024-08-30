# Podemos tener un diccionario anidado, 
# es decir, un diccionario dentro de otro diccionario
# Ejemplo:
estudiantes = {
    # En este diccionario, los nombres son la clave, para subdiccionarios
    'Peter': {  
        'age': 10, 
        'address': 'Lisbon'
    },
    'Isabel': 
        {'age': 11, 
        'address': 'Sesimbra'
    },
    'Anna': 
        {'age': 9, 
        'address': 'Lisbon'
    },
}
# Determinar tamaño de neustro diccionario
# COn la función len() podemos determinar el tamaño de nuestro diccionario
print(len(estudiantes))
