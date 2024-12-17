import matplotlib.pyplot as plt

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estado = "disponible"  # Estado del libro, inicialmente disponible

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "prestado"]:
            self.__estado = nuevo_estado

    def __str__(self):
        return f"{self.__titulo} de {self.__autor} (ISBN: {self.__isbn}) - {self.__estado}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.estado == "disponible":
            libro.estado = "prestado"
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado el libro: {libro}")
        else:
            print(f"El libro {libro} no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.estado = "disponible"
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro: {libro}")
        else:
            print(f"{self.nombre} no tiene el libro {libro}.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def graficar_estado_libros(self):
        # Contar libros disponibles y prestados
        disponibles = sum(1 for libro in self.libros if libro.estado == "disponible")
        prestados = len(self.libros) - disponibles

        # Crear el gráfico
        estados = ["Disponibles", "Prestados"]
        cantidades = [disponibles, prestados]

        plt.bar(estados, cantidades, color=["green", "red"])
        plt.title("Estado de los Libros en la Biblioteca")
        plt.xlabel("Estado")
        plt.ylabel("Cantidad")
        plt.show()

    def graficar_libros_prestados_por_usuario(self):
        # Contar los libros prestados por cada usuario
        usuarios = [usuario.nombre for usuario in self.usuarios]
        libros_prestados = [len(usuario.libros_prestados) for usuario in self.usuarios]

        # Crear el gráfico
        plt.bar(usuarios, libros_prestados, color="blue")
        plt.title("Cantidad de Libros Prestados por Usuario")
        plt.xlabel("Usuario")
        plt.ylabel("Cantidad de Libros Prestados")
        plt.show()

# Ejemplo de uso
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro("1984", "George Orwell", "978-0-452-28423-4")
usuario1 = Usuario("Juan", 1)
usuario2 = Usuario("Ana", 2)

biblioteca = Biblioteca()

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_usuario(usuario2)

# Mostrar lista de libros
biblioteca.listar_libros()

# Préstamos y devoluciones
usuario1.prestar_libro(libro1)
usuario2.prestar_libro(libro2)
usuario1.devolver_libro(libro1)

# Gráficos
biblioteca.graficar_estado_libros()  # Mostrar libros disponibles vs. prestados
biblioteca.graficar_libros_prestados_por_usuario()  # Mostrar libros prestados por usuario

