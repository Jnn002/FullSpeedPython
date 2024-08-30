class Fibonacci:
    def __init__(self, limite):
        self.x = 0
        self.y = 1
        self.limite = limite
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.x > self.limite:
            raise StopIteration
        estado = self.x
        self.x, self.y = self.y, self.x + self.y
        return estado

rango = Fibonacci(limite = int(input('Ingresa el limite: ')))

for item in rango:
    print(item)