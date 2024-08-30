# Encontrar el valor más alto de un diccionario
def busqueda(edad):
    valor = list(edad.values()) # Se obtienen los valores del diccionario
    key = list(edad.keys())     # Se obtienen las llaves del diccionario
    return key[valor.index(max(valor))]
# Diccionario
edad = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 12,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

print(busqueda(edad))