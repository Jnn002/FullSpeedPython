# Clases en Python

# Las clases en Python son un tipo de estructura que permite agrupar datos y funciones en un solo objeto.
class Persona:
    # El método __init__ es un método especial que se ejecuta al crear un objeto de la clase.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Los métodos de una clase se definen de la misma forma que una función, pero dentro de la clase.
    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años')
# Para crear un objeto de una clase, se debe llamar al nombre de la clase seguido de paréntesis.
a = Persona('Juan', 25)
# Para acceder a los atributos de un objeto, se debe usar la notación de punto.
a.saludar()