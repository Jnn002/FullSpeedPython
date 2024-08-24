# Dividir una sublista en dos sublistas

def getSubList():
    # Definimos nuestra lista
    s = [1, 4, 9, 10, 23]
    # Composición de sublistas
    s1 = s[0:3]
    s2 = s[3:] 
    return [s1, s2]
# Llamamos a la función
[s1, s2] = getSubList()
print(s1)
print(s2)