# El programa busca un caracter dentro de una cadena y devuelve su posición.
def buscar_caracter(cadena, caracter):

    # La posición del caracter dentro de la cadena.
    # El metodo find() devuelve la posicion del caracter en la cadena.
    posicion = cadena.find(caracter)
    # Si no se encuentra, devuelve -1.
    if posicion == -1:
        # Imprime un mensaje indicando que no se encontro el caracter.
        print(f"No se encuentra el caracter '{caracter}' en la cadena.")
        # Pregunta si desea intentar buscar otro caracter
        if preguntar_si_quiere_intentarlo_nuevamente():
            # Si se desea intentar nuevamente, pide el nuevo caracter a buscar.
            caracter = input("Ingrese el caracter que desea buscar: ")
            # Llama a la funcion buscar_caracter() nuevamente con el nuevo caracter.
            buscar_caracter(cadena, caracter)
    else:
        # Imprime un mensaje indicando la posición del caracter en la cadena.
        print(f"El caracter '{caracter}' se encuentra en la posición {posicion}.")


# Pregunta si desea intentar buscar otro caracter
def preguntar_si_quiere_intentarlo_nuevamente():
    while True:
        # Pide que se ingrese S (si) o N (no)
        eleccion_Si_No = input("¿Desea intentar buscar otro caracter? S/N: ")
        # Convierte la entrada del usuario a mayúsculas para comparar con "S" o "N".
        if eleccion_Si_No.upper() == "S":
            # Si el usuario ingresa S, devuelve True para indicar que desea intentar nuevamente.
            return True
        elif eleccion_Si_No.upper() == "N":
            # Si el usuario ingresa N, imprime un mensaje de cierre y devuelve False.
            print("Ok cerrando programa...")
            return False
        else:
            # Si el usuario ingresa algo diferente de S o N, pide que ingrese nuevamente.
            print("Ingrese S o N, porfavor.")


# Ejemplo de uso
# cadena: La cadena de texto en la que se busca.
cadena = input("Ingrese una palabra: ")
# caracter: El caracter que se quiere encontrar.
caracter = input("Ingrese el caracter que desea buscar: ")
# Llama a la función buscar_caracter() con la cadena y el caracter ingresados.
buscar_caracter(cadena, caracter)