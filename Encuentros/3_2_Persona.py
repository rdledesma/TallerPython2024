class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

"""
En Python, los operadores de comparación como <, >, <=, >=, etc., pueden ser personalizados para trabajar con objetos de clases que tú defines. Esto se hace implementando métodos especiales dentro de la clase. Algunos de estos métodos son:

    __lt__(self, other) → Define el comportamiento del operador <.
    __gt__(self, other) → Define el comportamiento del operador >.
    __eq__(self, other) → Define el comportamiento del operador ==.
    __le__(self, other) → Define el comportamiento del operador <=.
    __ge__(self, other) → Define el comportamiento del operador >=.
"""

# Crear dos objetos
persona1 = Persona("Ana", 25, "Madrid")
persona2 = Persona("Luis", 16, "Barcelona")

# Comparar edades
if persona1 < persona2:
    print(f"{persona1.nombre} es más joven que {persona2.nombre}.")
else:
    print(f"{persona2.nombre} es más joven que {persona1.nombre}.")

