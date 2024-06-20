import re

# Clase Socio
class Socio:
    def __init__(self, nombre, apellido, dni):
        # Inicializar atributos del socio
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.planes = []  # lista de planes del socio

    def agregar_plan(self, plan):
        # Agregar un plan a la lista de planes del socio
        self.planes.append(plan)

    def verificar_dni(self):
        # Verificar que el DNI tenga 10 dígitos
        while True:
            DNI = input("Cual es su DNI: ")
            # Verificar que el DNI sea un número de 10 dígitos
            if re.match(r"^\d{10}$", DNI):
                self.dni = DNI
                break
            else:
                print("El DNI debe tener 10 dígitos")

    def informacion(self):
        # Solicitar información del socio
        self.nombre = input("Cual es su nombre: ")
        self.apellido = input("Cual es su apellido: ")
        self.verificar_dni()

    def __str__(self):
        # Representación del socio como cadena
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"

# Clase Plan
class Plan:
    def __init__(self, nombre, descripcion, precio):
        # Inicializar atributos del plan
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        # Representación del plan como cadena
        return f"{self.nombre} - {self.descripcion} - Precio: {self.precio}"

# Clase Clase
class Clase:
    def __init__(self, nombre, descripcion, instructor):
        # Inicializar atributos de la clase
        self.nombre = nombre
        self.descripcion = descripcion
        self.instructor = instructor

    def __str__(self):
        # Representación de la clase como cadena
        return f"{self.nombre} - {self.descripcion} - Instructor: {self.instructor.nombre}"

# Clase Instructor
class Instructor:
    def __init__(self, nombre, apellido):
        # Inicializar atributos del instructor
        self.nombre = nombre
        self.apellido = apellido
        self.clases = []  # lista de clases del instructor

    def agregar_clase(self, clase):
        # Agregar una clase a la lista de clases del instructor
        self.clases.append(clase)

    def __str__(self):
        # Representación del instructor como cadena
        return f"{self.nombre} {self.apellido}"

# Crear objetos
socio1 = Socio("", "", "")
socio1.informacion()
socio2 = Socio("", "", "")
socio2.informacion()

plan1 = Plan("Plan básico", "Acceso a las instalaciones", 50)
plan2 = Plan("Plan premium", "Acceso a las instalaciones y clases personalizadas", 100)

clase1 = Clase("Yoga", "Clase de yoga para principiantes", Instructor("Ana", "Rodríguez"))
clase2 = Clase("Spinning", "Clase de spinning para avanzados", Instructor("Juan", "López"))

instructor1 = Instructor("Ana", "Rodríguez")
instructor2 = Instructor("Juan", "López")

instructor1.agregar_clase(clase1)
instructor2.agregar_clase(clase2)

socio1.agregar_plan(plan1)
socio2.agregar_plan(plan2)

# Imprimir información
print("Socios:")
print(socio1)
print(socio2)

print("\nPlanes:")
print(plan1)
print(plan2)

print("\nClases:")
print(clase1)
print(clase2)

print("\nInstructores:")
print(instructor1)
print(instructor2)