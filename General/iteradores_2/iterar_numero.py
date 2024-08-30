# iterador de números
class Numeros:
    def __iter__(self): 
        self.a = 1
        return self

    def __next__(self):
        if self.a <= rango:
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration
# instanciar la clase
clase = Numeros()
# iterar la clase
iterador = iter(clase)
# rango de números a iterar
rango = int(input("Ingrese el rango de números a iterar: "))

# imprimir los números
for x in iterador:
    print(f'Numero de iteración: {x}')