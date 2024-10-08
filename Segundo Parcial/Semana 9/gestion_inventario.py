class Producto:
    def __init__(self, ID_producto, nombre_producto, cantidad_producto, precio_producto):
        self.ID_producto = ID_producto
        self.nombre_producto = nombre_producto
        self.cantidad_producto = cantidad_producto
        self.precio_producto = precio_producto

    def __str__(self):
        return f"\n{self.nombre_producto}\nCantidad: {self.cantidad_producto}\nPrecio: ${self.precio_producto}"


class Inventario:
    def __init__(self):
        self.lista_productos = []

    def agrega_producto(self, producto):
        if any(p.ID_producto == producto.ID_producto for p in self.lista_productos):
            print("El producto ya existe")
        else:
            self.lista_productos.append(producto)

    def elimina_producto(self,ID_producto):
        for i, producto in enumerate(self.lista_productos):
            if producto.ID_producto == ID_producto:
                del self.lista_productos[i]
                print("Producto eliminado.")
                return
        print ("NO se encuentra el producto")

    def actualiza_producto(self, ID_producto, cantidad=None, precio=None):
        for producto in self.lista_productos:
            if producto.ID_producto == ID_producto:
                if cantidad is not None:
                    producto.cantidad_producto = cantidad
                if precio is not None:
                    producto.precio_producto = precio
                print("Se ha actualizado el producto.")
                return
        print("El producto no existe")

    def busca_producto(self, nombre):
        resultados = [p for p in self.lista_productos if nombre.lower() in p.nombre_producto.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def muestra_inventario(self):
        if self.lista_productos:
            for producto in self.lista_productos:
                print(producto)
        else:
            print("El inventario esta vacio")


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir producto\n2. Borrar producto\n3. Actualizar producto\n4. Buscar producto\n5. Mostrar inventario\n6. Salir")
        opciones = int(input("Ingrese una opcion: "))
        if opciones == 1:
            id_producto = input("Ingrese la ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            product0 = Producto(id_producto, nombre, cantidad, precio)
            inventario.agrega_producto(product0)
        elif opciones == 2:
            id_producto = input("Ingrese la id del producto para borrarlo: ")
            inventario.elimina_producto(id_producto)
        elif opciones == 3:
            id_producto = input("Ingrese la id del producto para actualizarlo: ")
            cantidad = input("Ingrese la cantidad del producto (deje en blanco para no cambiar): ")
            precio = input("Ingrese el precio del producto (deje en blanco para no cambiar) ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualiza_producto(id_producto, cantidad, precio)
        elif opciones == 4:
            nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
            inventario.busca_producto(nombre_buscado)
        elif opciones == 5:
            inventario.muestra_inventario()
        elif opciones == 6:
            break


if __name__ == "__main__":
    menu()
