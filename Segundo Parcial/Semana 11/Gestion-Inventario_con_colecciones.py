class Producto:
    def __init__(self, ID_producto, nombre_producto, cantidad_producto, precio_producto):
        self.ID_producto = ID_producto
        self.nombre_producto = nombre_producto
        self.cantidad_producto = cantidad_producto
        self.precio_producto = precio_producto

    def __str__(self):
        return f"{self.ID_producto}\nNombre:{self.nombre_producto}\nCantidad: {self.cantidad_producto}\nPrecio: ${self.precio_producto}\n"

    @classmethod
    def obtener_string(cls, string):
        # Crea una instancia de Producto a partir de una cadena de texto
        # La cadena debe tener el formato "ID, nombre, cantidad, precio"
        id_producto, nombre, cantidad, precio = string.strip().split(",")
        return cls(id_producto, nombre, cantidad, float(precio))


class Inventario:

    def __init__(self, datos_inventario="inventario.txt"):
        self.datos_inventario = datos_inventario
        # Lista cambiada por una colección - diccionario
        self.lista_productos = {}
        self.carga_inventario()

    def carga_inventario(self):
        # Carga los productos del archivo de datos en la lista de productos
        try:
            # Abre el archivo en modo lectura
            with open(self.datos_inventario, "r") as f:
                encontrado = False
                # Lee cada línea del archivo
                for linea in f:
                    # Crea un producto a partir de cada línea del archivo
                    producto = Producto.obtener_string(linea)
                    # Escribe el producto en la lista
                    self.lista_productos[producto.ID_producto] = producto
                    encontrado = True
                if encontrado:
                    print("Datos existentes en el inventario:")
                    for producto in self.lista_productos.values():
                        print(producto)
                else:
                    # Si no hay líneas en el archivo, muestra un mensaje
                    print("No hay datos en el archivo")
        except FileNotFoundError:
            # Si el archivo no existe lo crea
            with open(self.datos_inventario, "w") as f:
                print(f"El archivo {self.datos_inventario} no existe. Creando el archivo")
        except Exception as error:
            # Maneja cualquier otro error que pueda ocurrir
            print(f"Error al cargar el inventario: {error}")

    def guardar_archivo(self):
        # Guarda la lista de productos en el archivo de datos
        try:
            with open(self.datos_inventario, "r+") as f:
                for producto in self.lista_productos.values():
                    # Escribe cada producto en una línea separada
                    f.write(f"{producto.ID_producto}, {producto.nombre_producto}, {producto.cantidad_producto}, {producto.precio_producto}\n")
        except PermissionError:
            # Si no hay permisos para escribir en el archivo, muestra un mensaje de error
            print(f"No hay permisos para abrir el archivo {self.datos_inventario}")
        except Exception as error:
            print(f"Error: {error}")

    def agrega_producto(self, producto):
        try:
            # Verifica si la id del producto ya existe en el inventario
            if producto.ID_producto in self.lista_productos:
                print(f"La id -{producto.ID_producto}- ya existe")
            else:
                # añade el producto a la lista de productos
                self.lista_productos[producto.ID_producto] = producto
                # Guarda la lista de productos en el archivo de datos
                self.guardar_archivo()
                print(f"Producto {producto.nombre_producto} agregado al inventario")
        except Exception as error:
            print(f"Error: {error}")

    def elimina_producto(self, Id_producto):
        try:
            # Busca el producto en la lista de productos
            if Id_producto in self.lista_productos:
                # Elimina el producto basado en el id
                del self.lista_productos[Id_producto]
                with open(self.datos_inventario, "w") as dato:
                    for producto in self.lista_productos.values():
                        dato.write(f"{producto.ID_producto}, {producto.nombre_producto}, {producto.cantidad_producto}, {producto.precio_producto}\n")
                print("Producto eliminado.")
                return
            # Si no se encuentra el producto, muestra un mensaje
            print("NO se encuentra el producto")
        except Exception as error:
            print(f"Error {error}")

    def actualiza_producto(self, ID_producto, cantidad=None, precio=None):
        try:
            # Busca el producto en la lista de productos
            if ID_producto in self.lista_productos:
                # Actualiza los atributos del producto
                if cantidad is not None:
                    self.lista_productos[ID_producto].cantidad_producto = cantidad
                if precio is not None:
                    self.lista_productos[ID_producto].precio_producto = precio
                self.guardar_archivo()
                print("Se ha actualizado el producto.")
                return
            print("El producto no existe")
        except Exception as error:
            print(f"Error {error}")

    def busca_producto(self, nombre):
        try:
            # Busca el producto en la lista de productos
            resultados = [p for p in self.lista_productos.values() if nombre.lower() in p.nombre_producto.lower()]
            if resultados:
                # Muestra cada producto encontrado
                for producto in resultados:
                    print(producto)
            else:
                # Si no se encuentra el producto, muestra un mensaje
                print("No se encontraron productos con ese nombre.")
        except Exception as error:
            print(f"Error: {error}")

    def muestra_inventario(self):
        try:
            if self.lista_productos:
                for producto in self.lista_productos.values():
                    print(producto)
            else:
                # Si la lista de productos está vacía, muestra un mensaje
                print("El inventario esta vacio")
        except Exception as error:
            print(f"{error}")


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir producto\n2. Borrar producto\n3. Actualizar producto\n4. Buscar producto\n5. Mostrar inventario\n6. Salir")
        opciones = int(input("Ingrese una opcion: "))
        match opciones:
            case 1:
                id_producto = input("Ingrese la ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = input("Ingrese la cantidad del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                product0 = Producto(id_producto, nombre, cantidad, precio)
                inventario.agrega_producto(product0)
            case 2:
                id_producto = input("Ingrese la id del producto para borrarlo: ")
                inventario.elimina_producto(id_producto)
            case 3:
                id_producto = input("Ingrese la id del producto para actualizarlo: ")
                cantidad = input("Ingrese la cantidad del producto (deje en blanco para no cambiar): ")
                precio = input("Ingrese el precio del producto (deje en blanco para no cambiar) ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualiza_producto(id_producto, cantidad, precio)
            case 4:
                nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
                inventario.busca_producto(nombre_buscado)
            case 5:
                inventario.muestra_inventario()
            case 6:
                break


if __name__ == "__main__":
    menu()
