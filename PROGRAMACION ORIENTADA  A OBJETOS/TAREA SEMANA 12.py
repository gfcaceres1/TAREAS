class Libro:
    def __init__(self, titulo, autores, categoria, isbn):
        self.titulo = titulo
        self.autores = autores
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autores: {', '.join(self.autores)}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}  # Usamos un diccionario para mapear ID a usuario

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró un libro con el ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print("El ID de usuario ya existe.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró un usuario con el ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]  # Acceder directamente al usuario
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("No se pudo realizar el préstamo.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.libros_prestados = [libro for libro in usuario.libros_prestados if libro.isbn != isbn]
            print(f"Libro con ISBN {isbn} devuelto por {usuario.nombre}.")
        else:
            print("No se pudo realizar la devolución.")

    def buscar_libros(self, query):
        resultados = []
        for libro in self.libros.values():
            if query.lower() in libro.titulo.lower() or any(query.lower() in autor.lower() for autor in libro.autores) or query.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        usuario = self.obtener_usuario(id_usuario)
        if usuario:
            print(f"Libros prestados por {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"No se encontró un usuario con el ID {id_usuario}.")

    def obtener_usuario(self, id_usuario):
        return self.usuarios.get(id_usuario)

# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("El señor de los anillos", ["J.R.R. Tolkien"], "Fantasía", "12345")
libro2 = Libro("1984", ["George Orwell"], "Ciencia ficción", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuario
usuario1 = Usuario("Juan Pérez", 1)
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("12345", 1)

# Buscar libros
resultados = biblioteca.buscar_libros("orwell")
print("Resultados de la búsqueda:")
for libro in resultados:
    print(libro)

# Listar libros prestados
biblioteca.listar_libros_prestados(1)
