import math as m
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    # Metodo para calcular el area del circulo
    def area(self):
        return m.pi * self.radio**2
    # Metodo para calcular el perimetro del circulo
    def perimetro(self):
        return 2 * m.pi * self.radio

# Entrada de nuestro valor de radio
radio = float(input('Ingrese el radio del circulo: '))

# Creacion de nuestro objeto circulo
circulo = Circulo(radio)

# Formateo de nuestras salidas
area_c = circulo.area()
perimetro_c = circulo.perimetro()

# Impresion de los resultados
print(f'El area del circulo es: {area_c:.3f}')
print(f'El perimetro del circulo es: {perimetro_c:.3f}')