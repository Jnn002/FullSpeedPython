# Encontrar la edad promedio de valores de un diccionarios

def avgEdad(estudiantes):
    edades = 0
    for x in estudiantes.values():
        edad = x['age']
        edades = edades + edad
    return edades / len(estudiantes)

estudiantes = {
    'Peter': 
        {  
        'age': 17, 
        'address': 'Lisbon'
        },
    'Isabel': 
        {'age': 19, 
        'address': 'Sesimbra'
        },
    'Anna': 
        {'age': 24, 
        'address': 'Lisbon'
        },
    'John': 
        {'age': 20, 
        'address': 'Sesimbra'
        },
    'Alejandra': 
        {'age' : 23,
        'address' : 'Guatemala'
        }
}

print(f'La edad promedio es: {avgEdad(estudiantes)}') 