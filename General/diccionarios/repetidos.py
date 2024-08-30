# Encontrar personas que vivan en la misma ciudad

def matchValores(address, estudiantes):
    nombres = []
    # Iterar sobre el diccionario
    for key, subdiccionario in estudiantes.items():
        # Iterar sobre los valores de cada subdiccionario
        for sublista in subdiccionario.values():
            # Si el valor es igual a la dirección, agregar el nombre a la lista
            if (sublista == address):
                # Agregar el nombre a la lista
                nombres.append(key)
    return sorted(nombres)

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
        }, 
    'Pedro': 
        {'age' : 25,
        'address' : 'Tokio'
        }
}
busqueda = matchValores(input('Ingrese la ciudad: '), estudiantes)
print(busqueda)