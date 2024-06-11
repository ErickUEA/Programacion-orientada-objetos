import datetime


# Clase que representa la información diaria del clima.
class Clima_diario:
    # Constructor de la clase.
    def __init__(self, fecha, temperatura_maxima, temperatura_minima, precipitacion):
        # Atributo y argumento: fecha (str) - Fecha del día.
        self.fecha = fecha
        # Atributo y argumento: temperatura_maxima (float) - Temperatura máxima del día.
        self.temperatura_maxima = temperatura_maxima
        # Atributo y argumento: temperatura_minima (float) - Temperatura mínima del día.
        self.temperatura_minima = temperatura_minima
        # Atributo y argumento: precipitacion (float) - Precipitación del día (en mm).
        self.precipitacion = precipitacion
    def rango_fecha(self, fecha):
        try:
            tiempo_fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d")
            fecha_minima = datetime.datetime(1924, 1, 1)
            fecha_maxima = datetime.datetime.today()
            if tiempo_fecha < fecha_minima or tiempo_fecha > fecha_maxima:
                raise ValueError("La fecha ingresada esta fuera del rango de 1924-01-01 y la fecha de hoy.")
            return fecha
        except ValueError as error:
            print(f"Ha habido un error: {error}")
            return None


    def verifica_temperatura(self, temperatura, minimo, maximo):
        while temperatura < minimo or temperatura > maximo:
            print(f"La temperatura debe ser mayor que {minimo} y menor que {maximo}")
            temperatura = float(input("Ingrese una temperatura válida (°C): "))
        return temperatura


    def verifica_precipita(self, precipitacion):
        while precipitacion < 0 or precipitacion > 200:
            print("La precipitación debe ser mayor que 0.00mm y menor que 200.00mm")
            precipitacion = float(input("Ingrese la precipitación (mm): "))
        return precipitacion


    # Método: ingresar_datos() - Permite ingresar los datos del clima para un día específico.
    def ingresar_datos(self):
        # Permite ingresar los datos del clima para un día específico.
        while True:
            fecha = self.rango_fecha(input("Ingrese la fecha (YYYY-MM-DD): "))
            if fecha:
                self.fecha = fecha
                break
        self.temperatura_maxima = self.verifica_temperatura(float(input("Ingrese la temperatura máxima (°C): ")), 0, 50)
        self.temperatura_minima = self.verifica_temperatura(float(input("Ingrese la temperatura mínima (°C): ")), -50, 10)
        self.precipitacion = self.verifica_precipita(float(input("Ingrese la precipitación (mm): ")))


    # Método: calcular_promedio() - Calcula el promedio de las temperaturas (máxima y mínima).
    def calcular_promedio(self):
        # Retorna: Promedio de las temperaturas.
        return (self.temperatura_maxima + self.temperatura_minima) / 2


    # mostrar_informacion(): Muestra la información del clima formateada.
    def mostrar_informacion(self):
        """
        Muestra la información del clima formateada.
        """
        print("┌----------------------------------------------------┐")
        print(f"| Fecha: {self.fecha}                                  |")
        print(f"| Temperatura máxima: {self.temperatura_maxima:.2f} °C                       |")
        print(f"| Temperatura mínima: {self.temperatura_minima:.2f} °C                        |")
        print(f"| Precipitación: {self.precipitacion:.2f} mm                            |")
        print(f"| Promedio de temperatura: {self.calcular_promedio():.2f} °C                  |")
        print("└----------------------------------------------------┘")


# Crear un objeto Clima_diario
dia_clima = Clima_diario("", 0, 0, 0)

# Ingresar datos para el día
dia_clima.ingresar_datos()

# Mostrar la información del clima
dia_clima.mostrar_informacion()
