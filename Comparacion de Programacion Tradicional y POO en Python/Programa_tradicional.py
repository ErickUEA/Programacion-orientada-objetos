# Función para ingresar la temperatura de un día específico.
def ingresar_temperatura_dia():
    i = 1
    while i <= 7:
        # Valida que la entrada sea un número válido.
        while True:
            try:
                # Solicita al usuario que ingrese la temperatura como un valor numérico.
                temperatura = float(input(f"Ingrese la temperatura del día {i}: "))
                # Verifica si la temperatura está entre -50 y 50
                if temperatura < -50 or temperatura > 50:
                    temperatura = float(input("Ingrese una temperatura mayor que -50 o menor que 50: "))
                break
            except ValueError:
                print("Ha ingresado una letra, intente de nuevo.")
        i += 1
    # Retorna la temperatura ingresada como un valor flotante.
    return temperatura


# Función para calcular el promedio semanal de temperaturas.
def calcular_promedio_semanal(temperaturas):
    # Recibe una lista de temperaturas como entrada.
    # Verifica que la lista no esté vacía.
    if not temperaturas:
        print("No hay temperaturas registradas.")
    # Calcula la suma de las temperaturas.
    suma_temperaturas = sum(temperaturas)
    # Divide la suma por la cantidad de temperaturas para obtener el promedio.
    promedio_semanal = suma_temperaturas / len(temperaturas)
    # Retorna el promedio semanal como un valor flotante.
    return promedio_semanal


temperaturas_semanales = []
#  Llama a la función `ingresar_temperatura_dia` para obtener las temperaturas de cada día.
temperatura_dia = ingresar_temperatura_dia()
#  Almacena las temperaturas en una lista.
temperaturas_semanales.append(temperatura_dia)
#  Llama a la función `calcular_promedio_semanal` para obtener el promedio semanal.
promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
#  Muestra el promedio semanal por pantalla.
print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")
