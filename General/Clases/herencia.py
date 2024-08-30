# Definición de clase Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        return 'El animal hace un sonido!'

# Definimos una clase derivada llamada Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
    # Las sublcasles pueden contar con atributos propios
        self.raza = raza

    def sonido(self):
        return 'El perro dice: ¡Guau!'

# Definimos una clase derivada llamada Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
    # Las subclases pueden contar con atributos propios
        self.color = color

    def sonido(self):
        return 'El gato dice: ¡Miau!'

# Creamos instancias de las clases Perro y Gato
mi_perro = Perro('Rex', 5, 'Labrador')
mi_gato = Gato('Miau', 3, 'Negro')

# Usamos los métodos de las instancias
print(f'Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años. {mi_perro.sonido()}')
print(f'Mi gato se llama {mi_gato.nombre} y tiene {mi_gato.edad} años. {mi_gato.sonido()}')
