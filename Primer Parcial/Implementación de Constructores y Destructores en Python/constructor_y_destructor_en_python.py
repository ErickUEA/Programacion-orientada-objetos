# Esta clase representa una cuenta bancaria básica.
class CuentaBancaria:
    # Metodo: __init__(self, titular, saldo_inicial)
    # Constructor. Inicializa el titular y el saldo de la cuenta.
    def __init__(self, titular, cedula, saldo_inicial):
        # titular (str): El nombre del titular de la cuenta.
        self.titular = titular
        # saldo_inicial (float, opcional): El saldo inicial de la cuenta (por defecto 0).
        self.saldo = saldo_inicial
        # cedula (str): El documento de identidad o cedula de la cuenta
        self.__cedula = cedula

    # Metodo: ingresar_informacion(self)
    # Pide al usuario ingresar la información de la cuenta.
    def ingresar_informacion(self):
        # ruta de un archivo de texto
        ruta = "Implementación de Constructores y Destructores en Python/clientes.txt"
        # abrimos el archivo en modo de escritura (a)
        archivo = open(ruta, "a")
        # pide que se ingrese el nombre
        titular_ingresado = input("Ingrese el nombre del titular: ")
        # llama al metodo de verificar cedula
        self.verifica_cedula()
        # pide que se ingrese el saldo
        saldo_ingresado = float(input("Cual es el saldo inicial: "))
        # transformamos a string el saldo
        saldo_string = str(saldo_ingresado)
        print(f"Cuenta creada para {self.titular} con CI: {self.__cedula} y un saldo inicial de ${saldo_string}")
        archivo.write(f"Titular: {titular_ingresado} Cedula: {self.__cedula} Saldo: {saldo_ingresado:.2f}\n")
        archivo.close()

    # Metodo: mostrar_informacion(self): Muestra la información de la cuenta (titular y saldo).
    def mostrar_informacion(self):
        """
        Muestra la información de la cuenta (titular, cedula y saldo).
        """
        print(f"Información de la cuenta:")
        print(f"Titular: {self.titular}")
        print(f"Cedula: {self.__cedula}")
        print(f"Saldo: ${self.saldo:.2f}")

    # Metodo: verificar_borrado(self)
    # Verifica si la cuenta puede ser eliminada.
    def verificar_borrado(self):
        print("Solo la cuenta puede ser eliminada si tiene mas de 5 años sin depositar dinero.")
        eleccion = input("Desea continuar. S/N: ")
        if eleccion.upper() == "S":
            print()
        else:
            print("Regresando al menu..")
            menu()

    # Metodo: verifica_cedula(self)
    # Verifica la cédula del titular.
    def verifica_cedula(self):
        # Pedir la cédula al usuario
        self.__cedula = input("Ingrese la cédula del titular: ")
        while True:
            # Verificar si la cédula tiene 10 dígitos
            if len(self.__cedula) != 10:
                print("La cédula debe tener 10 dígitos. Intente nuevamente.")
                self.__cedula = input("Ingrese nuevamente la cedula: ")
            else:
                # Inicializar variables
                suma_2 = 0
                suma_3 = 0
                # Calcular la suma de los dígitos impares y pares
                for incremento in range(10):
                    digito = int(self.__cedula[incremento])
                    # verifica que el residuo del incremento es 0
                    if incremento % 2 == 0:
                        # multiplica los numeros en posiciones impares por 2
                        impar = digito * 2
                        # Verifica que el impar sea mayor que 9
                        if impar > 9:
                            # Si es mayor entonces se le resta 9
                            impar -= 9
                        # Guardamos las respuestas en la variable suma_2
                        suma_2 += impar
                    else:
                        # Aqui solo se suman los digitos en posiciones pares
                        # no hay multiplicación debido a que solo se tiene que multiplicar por 1
                        suma_3 += digito

                # Calcular el dígito verificador
                suma_total = suma_2 + suma_3
                # Divide la suma total entre 10
                division = suma_total / 10
                # Transforma la respuesta de la division a entero
                entero = int(division)
                # Le suma 1 al valor entero de la division y luego lo multiplica por 10
                aumento = (entero + 1) * 10
                # Resta el aumento y la suma total
                comprobador = aumento - suma_total
                # extrae el último dígito de la cédula de identidad y lo convierte a un entero.
                verificador = int(self.__cedula[9])

                # Verificar si la cédula es correcta
                if comprobador == verificador or comprobador == 10:
                    print("Cédula correcta")
                    break
                else:
                    print("Cédula incorrecta.")
                    self.__cedula = input("Intente nuevamente: ")

    # Metodo: borrar_cuenta(self)
    # Elimina la cuenta.
    def borrar_cuenta(self):
        ruta = "Implementación de Constructores y Destructores en Python/clientes.txt"
        archivo = open(ruta, "r")
        print("Mostrando todas las cuentas disponibles...")
        if len(archivo.readlines(0)) == 0:
            print("No hay cuentas tiene que crear una. \n Regresando al menu...")
            menu()
        else:
            print("Cuentas disponibles")
            archivo = open(ruta, "r")
            for linea in archivo.readlines():
                print(linea)
            archivo.close()
            self.verificar_borrado()

    # Metodo: __del__(self)
    # Destructor. Imprime un mensaje cuando se elimina la cuenta.
    def __del__(self):
        # Se ejecuta automáticamente cuando se elimina la instancia de la cuenta.
        print(f"Cuenta eliminada")


cuenta1 = CuentaBancaria("", "", "")


def menu():
    opcion = -1
    while opcion != 3:
        print("Bienvenido al menu que desea hacer:"
              "\n1. Crear Cuenta"
              "\n2. Eliminar Cuenta")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                cuenta1.ingresar_informacion()
            case 2:
                cuenta1.borrar_cuenta()
                break
            case _:
                print("Opcion incorrecta")


menu()
