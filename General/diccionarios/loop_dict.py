
# Estructura de un diccionario en Python
# Un dicccinonario esta dividido en 
# llaves y valores
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
# Imprimir los valores del diccionario
""" for x in ages:
    print(ages[x]) """
# Imprimir las llaves del diccionario
""" for x in ages:
    print(x) """
# Imprimir las llaves y los valores del diccionario
for nombre, edad in ages.items():
    print(nombre, edad)