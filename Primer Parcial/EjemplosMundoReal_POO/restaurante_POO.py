# Importar modulos necesarios
import datetime
import re


# Clase Cliente
class Cliente:
    def __init__(self, nombre, informacion_de_contacto):
        # Inicializar objeto Cliente con nombre y contacto
        self.nombre = nombre
        self.informacion_de_contacto = informacion_de_contacto

    def datos(self):
        # Solicita al usuario que ingrese su nombre
        self.nombre = input("Cual es su nombre: ")
        while True:
            contacto = input("Cual es su contacto: ")
            # Verificar que el contacto sea un número de teléfono con 10 dígitos o un email válido
            if re.match(r"^\d{10}$", contacto):
                self.informacion_de_contacto = contacto
                break
            elif re.match(r"[^@]+@[^@]+\.[^@]", contacto):
                self.informacion_de_contacto = contacto
                break
            else:
                print("El contacto debe ser un número de teléfono con 10 dígitos o un email válido")
    def __str__(self):
        # Devolver una representación de cadena del objeto Cliente
        return (f"Nombre: {self.nombre}"
                f"\nContacto: {self.informacion_de_contacto}")

# Clase Mesa
class Mesa:
    def __init__(self, numero_de_mesa):
        # Inicializar objeto Mesa con número de mesa
        self.numero_de_mesa = numero_de_mesa
        self.reservas = []

    def agregar_reserva(self, reserva):
        # Agregar una reserva a la mesa
        self.reservas.append(reserva)

    def asignar_mesa(self):
        # Solicitar al usuario que ingrese un número de mesa
        while True:
            n_mesa = int(input("Ingrese numero de mesa: "))
            if n_mesa < 0:
                print("El numero debe ser positivo ingreselo denuevo: ")
            else:
                self.numero_de_mesa = n_mesa
                break


# Clase Reserva
class Reserva:
    def __init__(self, cliente, fecha, hora):
        # Inicializar objeto Reserva con cliente, fecha y hora
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def rango_fecha(self, fecha):
        # Verificar que la fecha ingresada esté dentro del rango de hoy y dos años en el futuro
        try:
            tiempo_fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d")
            fecha_minima = datetime.datetime.today()
            fecha_maxima = fecha_minima + datetime.timedelta(days=365 * 2)
            fecha_maxima.strftime("%Y-%m-%d")
            if tiempo_fecha < fecha_minima or tiempo_fecha > fecha_maxima:
                raise ValueError(f"La fecha ingresada esta fuera del rango de hoy y {fecha_maxima}.")
            return fecha
        except ValueError as error:
            print(f"Ha habido un error: {error}")
            return None

    def verificar_hora(self, hora):
        # Verificar que la hora ingresada sea válida
        try:
            hour = datetime.datetime.strptime(hora, "%H:%M:%S")
            return hour
        except ValueError:
            print("La hora no es valida")
            return None

    def ingresar_reserva(self):
        # Solicitar al usuario que ingrese la fecha y hora de la reserva
        while True:
            fecha = self.rango_fecha(input("Ingrese la fecha de reservacion: "))
            if fecha:
                self.fecha = fecha
                break
        while True:
            hora = self.verificar_hora(input("Ingrese la hora de la reservacion: "))
            if hora:
                self.hora = hora
                break

    def __str__(self):
        # Devolver una representación de cadena del objeto Reserva
        return (f"Fecha de reservacion: {self.fecha}"
                f"\nHora de la reservacion: {self.hora.strftime('%H:%M:%S')}")


# Clase Plato
class Plato:
    def __init__(self, nombre, descripcion, precio):
        # Inicializar objeto Plato con nombre, descripción y precio
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def verifica_precio(self):
        # Solicitar al usuario que ingrese un precio y verificar que sea positivo
        while True:
            precio = float(input("Cuanto desea pagar: "))
            if precio < 0:
                print("El precio es negativo. Ingreselo denuevo: ")
            else:
                self.precio = precio
                break

    def ingresar_plato(self):
        # Solicitar al usuario que ingrese el nombre, descripción y precio del plato
        self.nombre = input("Que plato desea pedir: ")
        self.descripcion = input("Cual es la descripcion del plato: ")
        self.verifica_precio()

# Clase Pedido
class Pedido:
    def __init__(self, mesa, platos):
        # Inicializar objeto Pedido con mesa y lista de platos
        self.mesa = mesa
        self.platos = platos


# Clase Restaurante
class Restaurante:
    def __init__(self):
        # Inicializar objeto Restaurante con listas vacías para mesas, menú y pedidos
        self.mesas = []
        self.menu = []
        self.pedidos = []

    def agregar_mesa(self, mesa):
        # Agregar una mesa al restaurante
        if mesa not in self.mesas:
            self.mesas.append(mesa)

    def agregar_plato_al_menu(self, plato):
        # Agregar un plato al menú del restaurante
        if plato not in self.menu:
            self.menu.append(plato)

    def crear_pedido(self, mesa, platos):
        # Crear un nuevo pedido con una mesa y una lista de platos
        pedido = Pedido(mesa, platos)
        self.pedidos.append(pedido)
        return pedido


# Ejemplo de uso
restaurante = Restaurante()
cliente1 = Cliente("", "")
cliente1.datos()
mesa1 = Mesa("")
mesa1.asignar_mesa()
reserva1 = Reserva(cliente1, "", "")
reserva1.ingresar_reserva()
mesa1.agregar_reserva(reserva1)
plato1 = Plato("", "", "")
plato1.ingresar_plato()
plato2 = Plato("", "", "")
plato2.ingresar_plato()
restaurante.agregar_plato_al_menu(plato1)
restaurante.agregar_plato_al_menu(plato2)
platos_pedidos = [plato1, plato2]
print("----------------------------------------------------------------------")
print(cliente1)
print(reserva1)
pedido = restaurante.crear_pedido(mesa1, platos_pedidos)
print(f"Pedido para la mesa {pedido.mesa.numero_de_mesa}:")
for plato in pedido.platos:
    print(f"- {plato.nombre}-{plato.descripcion}: ${plato.precio}")
print("-----------------------------------------------------------------------")