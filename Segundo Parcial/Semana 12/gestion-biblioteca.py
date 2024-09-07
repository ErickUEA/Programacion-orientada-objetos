class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # el titulo y el autor se guardan en una tupla para no ser modificados
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    # retorna el titulo
    def titulo(self):
        return self.titulo_autor[0]

    @property
    # retorna el autor
    def autor(self):
        return self.titulo_autor[1]

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # los libros prestados al usuario se guardan en una lista
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        # los libros se guardan en un diccionario
        self.libros = {}
        # los usuarios registrados se guardan en un diccionario clave-valor
        self.usuarios = {}
        # se guarda las id de los usuarios en un conjunto y nunca guardara valores repetidos
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        # Si la isbn del libro no se encuentra
        if libro.isbn not in self.libros:
            # Se añade al diccionario los valores ingresados
            self.libros[libro.isbn] = libro
            # Mensaje que se ha añadido con existo el libro
            print(f"Se ha añadido el libro {libro.titulo}")
        else:
            print("El libro ya existe")

    def quitar_libro(self, isbn):
        # Si la isbn existe se elimina el libro si no sale un mensaje
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN -{isbn}- eliminado")
        else:
            print("El libro no existe")

    def registra_usuario(self, usuario):
        # Si la id del usuario no existe en el conjunto
        if usuario.id_usuario not in self.ids_usuarios:
            # Se añade el nombre del usuario al diccionario
            self.usuarios[usuario.id_usuario] = usuario
            # Se agrega al conjunto la id del usuario y luego se añade al diccionario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario añadido")
        else:
            print("ya existe el usuario")

    def dar_de_baja_usuario(self, id_usuario):
        # Si existe la id se elimina el usuario
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con id -{id_usuario}- eliminado")
        else:
            print("El usuario no se ha encontrado")

    def presta_libro(self, id_usuario, isbn):
        # Si la id y el isbn existen
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            # Se agrega los datos del libro a la lista de libros prestados
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]
            print(f"Libro {libro.titulo} prestado a {usuario.nombre}")
        else:
            print("Libro o usuario no existen")

    def devolver_libro(self, id_usuario, isbn):
        # si la id esta en el diccionario
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            # recorre los libros prestados
            for libro in usuario.libros_prestados:
                # si la isbn ingresada existe en los libros prestados
                if libro.isbn == isbn:
                    # se elimina de los libros
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro {libro.titulo} devuelto por el usuario {usuario.nombre}")
                    break

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        # Se guarda los resultados en una lista
        resultados = []
        # Recorre los valores del libro
        for libro in self.libros.values():
            # si el titulo o autor o categoria existen se añade a la lista de resultados
            if (titulo and titulo in libro.titulo) or \
               (autor and autor in libro.autor) or \
               (categoria and categoria == libro.categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        #Si la id existe
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            # Regresa la lista de libros prestados
            return usuario.libros_prestados
        return []


def menu():
    biblioteca = Biblioteca()
    while True:
        # \033 sirve para poner color con el codigo ansii 1 es negrita y 34 es color de texto azul
        # para saber mas codigos ascii https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
        print("\n\033[1;34mBienvenido al menu\033[0m ≡\t\033[1;32m¿que desea realizar?\033[0m\n\033[1;30;5m1.\033[0m Añadir un libro📗\t\033[1;30;5m2. \033[0mEliminar un libro"
              "\n\033[1;30;5m3. \033[0mRegistrar a un usuario🙍‍♂️ \t\033[1;30;5m4. \033[0mDar de baja a un usuario\n\033[1;30;5m5. \033[0mPrestar un libro📕\t\t\033[1;30;5m6. \033[0mRegresar un libro\n\033[1;30;5m7. \033[0mBuscar libros 📚 \t\033[1;30;5m8. \033[0mMostrar una lista de los libros prestados"
              "\n\033[1;30;5m9. \033[0mSalir")
        # bloque try que verificare si el tipo de dato ingresado es correcto
        try:
            opciones = int(input("Ingrese una opcion: "))
            match opciones:
                case 1:
                    titulo = input("Ingrese el titulo del libro: ")
                    autor_autores = input("Ingrese el autor o autores de la obra: ")
                    categoria = input("Ingrese de que categoria es: ")
                    isbn = input("Ingrese el International Standar Book Number(ISBN): ")
                    libr0 = Libro(titulo, autor_autores, categoria, isbn)
                    biblioteca.añadir_libro(libr0)
                case 2:
                    isbn = input("Ingrese el ISBN para eliminar el libro. ")
                    biblioteca.quitar_libro(isbn)
                case 3:
                    user = input("Cual es el nombre del cliente: ")
                    id_user = input("Ingrese la identifcacion del cliente: ")
                    usuario = Usuario(user, id_user)
                    biblioteca.registra_usuario(usuario)
                case 4:
                    id_usuario = input("Ingrese la id del usuario para eliminarlo: ")
                    biblioteca.dar_de_baja_usuario(id_usuario)
                case 5:
                    usuario_id = input("Ingrese la id del usuario al que se va a prestar: ")
                    Isbn = input("Ingrese el isbn del libro para prestarlo: ")
                    biblioteca.presta_libro(usuario_id, Isbn)
                case 6:
                    ISbn = input("Ingrese el ISBN del libro a devolver: ")
                    Id_user = input("Ingrese el id del usuario al que presto el libro: ")
                    biblioteca.devolver_libro(ISbn, Id_user)
                case 7:
                    titulo = input("Titulo del libro que desea buscar: ")
                    resultados = biblioteca.buscar_libro(titulo)
                    if len(resultados) != 0:
                        print(f"Se ha encontrado el libro\nTitulo: {[libro.titulo for libro in resultados]} Autor: {[libro.autor for libro in resultados]} Categoria: {[libro.categoria for libro in resultados]} ISBN: {[libro.isbn for libro in resultados]}")
                    else:
                        print("No existe o no se ha creado el libro")
                case 8:
                    user_id = input("Ingrese id del usuario para revisar que libros fueron prestados: ")
                    print(f"libro/os: {[libro.titulo for libro in biblioteca.listar_libros_prestados(user_id)]} prestado/s a {usuario.nombre}")
                case 9:
                    break
        # Si se ingresa un valor erroneo sale error y regresa al bucle
        except ValueError:
            print(f"Error tipo de dato incorrecto, intente nuevamente.")



if __name__ == "__main__":
    menu()


"""
i = 0

biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "1")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "2")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)


# Registrar usuario
usuario1 = Usuario("Juan Pérez", "1")
biblioteca.registra_usuario(usuario1)
print(f"registro {usuario1.id_usuario}")
while True:
    usuario_id = input("Ingrese la id del usuario al que se va a prestar: ")
    Isbn = input("Ingrese el isbn del libro para prestarlo: ")
    biblioteca.presta_libro(usuario_id, Isbn)


# Prestar libro
biblioteca.presta_libro("001", "1234567890")
biblioteca.presta_libro("001", "234")

# Listar libros prestados
print("libro prestado")
print([libro.titulo for libro in biblioteca.listar_libros_prestados("001")])
print("-------------------------")
# Devolver libro
biblioteca.devolver_libro("001", "1234567890")

# Buscar libro
print("------------------------------")
resultados = biblioteca.buscar_libro(titulo="o")
print([libro.titulo for libro in resultados])
"""