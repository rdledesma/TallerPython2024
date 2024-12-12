# Definición de la clase
class Persona:
    # Constructor
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
	self.ciudad = ciudad
    # Método para saludar
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy de {self.ciudad}")



##1) añadir un método que retorne verdadero o falso si la persona es o no mayor de edad

##2) añade un método que permita cambiar la ciudad de una Persona

# Crear un objeto (instancia) de la clase
persona1 = Persona("Ana", 25, "Salta")

# Llamar a un método
persona1.presentarse()

