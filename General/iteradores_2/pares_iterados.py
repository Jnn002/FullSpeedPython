class Rangopares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        pares = [] 
        for i in range(1, self.n+1):
            # Validación de número par
            if i % 2 == 0: 
                pares.append(i) # Si es par será agregado a la lista
        return pares
# Instancia de la clase
myrange = Rangopares(int(input('Ingresa el limite superior del rango: ')))
# impresión 
print (myrange.next())