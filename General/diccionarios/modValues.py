# Aumentar el valor de los valores de un diccionario en 
#* Los diccionarios no puedes ser accedidos por indices, solo por llaves
# Definos nuestra función y parametros de entrada
def aumento(edad, n = 1):
    # x es cada item de nuestro diccionario
    # x0 => Peter, x1 => Isabel etc., 
    for x in edad:
        edad[x] += n
    return edad
    
edades = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 12,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
edad_actualizada = aumento(edades, 1)
print(edad_actualizada)

# IMPRIMIR UN VALOR ESPECIFICO
#print(aumento(edades, 1)['Anna']) # Imprime la nueva edad de Anna