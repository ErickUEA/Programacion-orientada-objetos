# Clase base para representar a un empleado en la empresa.
class Empleado:
    def __init__(self, nombre, apellido, cedula):
        # __nombre (str): Nombre del empleado (privado).
        self.__nombre = nombre
        # __apellido (str): Apellido del empleado (privado).
        self.__apellido = apellido
        # __cedula (str): Cédula de identidad del empleado (privado).
        self.__cedula = cedula

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre_empleado(self):
        return self.__nombre
# metodo: get_nombre_completo()
    def get_nombre_completo(self):
        # Retorna el nombre completo del empleado.
        return f"{self.__nombre} {self.__apellido}"

# metodo: get_datos_empleado()
    def get_datos_empleado(self):
        # Muestra la información del empleado.
        print("Informacion del empleado a buscar")
        print(f"Nombre Completo: {self.get_nombre_completo()}")
        print(f"Cédula: {self.get_cedula()}")  # Se modifica para mostrar la cédula (solo accesible dentro de la clase)

# metodo para verificar la cedula del empleado
    def verifica_cedula(self):
        # Pedir la cédula al usuario
        self.__cedula = input("Ingrese la cédula del empleado: ")
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
    def ingresar_datos(self):
        self.__nombre = input("Cual es el nombre del empleado: ")
        self.__apellido = input("Cual es el apellido: ")
        self.verifica_cedula()

    def get_cedula(self):
        return self.__cedula


# Clase derivada para representar a un gerente en la empresa.
class Gerente(Empleado):
    def __init__(self, nombre, apellido, cedula, area_gestionada):
        # Atributos heredados:
        # __nombre (str): Nombre del empleado (privado).
        # __apellido (str): Apellido del empleado (privado).
        # __cedula (str): Cédula de identidad del empleado (privado).
        super().__init__(nombre, apellido, cedula)
        # Atributo propio:
        # area_gestionada (str): Área que gestiona el gerente.
        self.area_gestionada = area_gestionada

# Método propio: Simula la gestión de empleados por parte del gerente.
    def gestionar_empleados(self):
        # Métodos heredados: get_nombre_completo() y get_datos_empleado()
        # Retorna el nombre completo del empleado y muestra la información del empleado.
        print(f"El gerente {self.get_nombre_completo()} está gestionando al empleado del área {self.area_gestionada}.")


# Clase derivada para representar a un vendedor en la empresa.
class Vendedor(Empleado):
    def __init__(self, nombre, apellido, cedula, productos_asignados):
        # Atributos heredados:
        # __nombre (str): Nombre del empleado (privado).
        # __apellido (str): Apellido del empleado (privado).
        # __cedula (str): Cédula de identidad del empleado (privado).
        # cargo (str): Cargo del empleado (Gerente o Vendedor).
        super().__init__(nombre, apellido, cedula)
        # Atributo propio:
        # productos_asignados (list): Lista de productos asignados al vendedor.
        self.productos_asignados = productos_asignados

# Método propio: Simula la venta de un producto por parte del vendedor.
    def vender_producto(self):
        # Retorna el nombre completo del empleado y muestra la información del empleado.
        print(f"El vendedor {self.get_nombre_completo()} está vendiendo el producto {self.productos_asignados}.")

    def ingresar_datos(self):
        self.set_nombre(input("Cual es el nombre del vendedor: "))
        self.vender_producto()


empleado = Empleado("", "", "")
gerente = Gerente("Danilo", "Fox", "0910985993", "contabilidad")
vendedor = Vendedor("", "", "", "tinta y papel")
while True:
    print("\nQue desea hacer:"
          "\nA. Ver quien esta gestionando a un empleado"
          "\nB. Ver que esta vendiendo un empleado"
          "\nC. Salir")
    opcion = input("Elija una opcion: ")
    if opcion.upper() == "A":
        empleado.ingresar_datos()
        empleado.get_datos_empleado()
        gerente.gestionar_empleados()
    elif opcion.upper() == "B":
        vendedor.ingresar_datos()
    else:
        print("Cerrando programa...")
        break
