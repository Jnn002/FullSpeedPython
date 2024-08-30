# Clase que nos permite calcular el area y perimetro de un rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # Metodo que nos permite calcular el area del rectangulo
    def area(self):
        return self.base * self.altura
    # Metodo que nos permite calcular el perimetro del rectangulo
    def perimetro(self):
        return 2 * (self.base + self.altura)
# Ingreso de nuestra base y altura del rectangulo
altura = int(input('Ingrese la altura del rectangulo: '))
base = int(input('Ingrese la base del rectangulo: '))

# Creacion de nuestro objeto rectangulo
rectangulo = Rectangulo(base, altura)

# Impresion de los resultados
print('El area del rectangulo es:', rectangulo.area())
print('El perimetro del rectangulo es:', rectangulo.perimetro())
