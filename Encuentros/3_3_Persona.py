class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otra_persona):
        return self.edad + otra_persona.edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


p1 = Persona("Ana", 30)
p2 = Persona("Luis", 25)

# Sumar edades
print(f"La suma de las edades es: {p1 + p2}")  # 55

# Mostrar información de las personas
print(p1)  # Nombre: Ana, Edad: 30
print(p2)  # Nombre: Luis, Edad: 25

