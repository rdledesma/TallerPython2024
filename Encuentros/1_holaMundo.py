#la función ´print´ es una función que me permite imprimir 'algun' mensaje
print("Hola")





# Diferentes tipos de datos
nombre = "Carlos"  # Cadena de texto (str)
edad = 28          # Entero (int)
altura = 1.75      # Decimal (float)
es_estudiante = False  # Booleano (bool)
hobbies = ["leer", "correr", "viajar"]  # Lista (list)
coordenadas = (10.5, -20.3)  # Tupla (tuple)
colores_favoritos = {"rojo", "azul"}  # Conjunto (set)
info_personal = {"nombre": "Carlos", "edad": 28}  # Diccionario (dict)
nada = None  # Ningún valor (NoneType)



#cómo ingresar por teclado

# 1. Entero
edad = int(input("Ingresa tu edad: "))
print(f"Tu edad es {edad}")

# 2. Decimal
altura = float(input("Ingresa tu altura en metros (por ejemplo, 1.75): "))
print(f"Tu altura es {altura} metros")

# 3. Cadena
nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}!")

# 4. Booleano
es_mayor_de_edad = input("¿Eres mayor de edad? (y/n): ").strip().lower() == "y"
print(f"Eres mayor de edad: {es_mayor_de_edad}")

# 5. Lista
hobbies = input("Ingresa tus hobbies separados por comas: ").split(",")
print(f"Tus hobbies son: {hobbies}")