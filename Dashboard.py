# importa el módulo os que proporciona una forma de utilizar funcionalidades del sistema operativo, como trabajar con rutas de archivos y directorios.
import os


# función mostrar_codigo que toma un parámetro ruta_script, que es la ruta del script que se quiere mostrar.
def mostrar_codigo(ruta_script):
    # Convierte la ruta del script en una ruta absoluta utilizando la función os.path.abspath. Esto asegura que la ruta sea válida y no relativa.
    ruta_script_absoluta = os.path.abspath(ruta_script)
    # Intenta abrir el archivo. Si el archivo se abre correctamente:
    try:
        # pone el archivo en modo de lectura ('r') utilizando la ruta absoluta
        with open(ruta_script_absoluta, 'r') as archivo:
            # imprime un título que indica el nombre del script
            print(f"\n--- Código de {ruta_script} ---\n")
            # imprime el contenido del archivo utilizando el método read().
            print(archivo.read())
    # Captura la excepción FileNotFoundError que se lanza si el archivo no se encuentra en la ruta especificada.
    except FileNotFoundError:
        # Imprime un mensaje de error indicando que el archivo no se encontró.
        print("El archivo no se encontró.")
    # Captura cualquier otra excepción que se lance durante la lectura del archivo.
    except Exception as e:
        # Imprime un mensaje de error indicando que ocurrió un error al leer el archivo y muestra el mensaje de error específico (e).
        print(f"Ocurrió un error al leer el archivo: {e}")


# Funcion mostrar menu sin parámetros
def mostrar_menu():
    # Obtiene la ruta base del archivo actual (__file__) utilizando la función os.path.dirname
    # Esta ruta base se utilizará para construir las rutas absolutas de los scripts.
    ruta_base = os.path.dirname(__file__)
    # Define un diccionario opciones que contiene las opciones del menú.
    # Cada clave es un número de opciones y el valor es la ruta del script correspondiente.
    opciones = {
        # opciones a escoger
        '1': 'EjemplosMundoReal_POO/restaurante_POO.py',
        '2': 'Implementación de Constructores y Destructores en Python/constructor_y_destructor_en_python.py',
        '3': 'EjemplosMundoReal_POO/gimnasio_POO.py'
    }


    while True:
        print("\nMenu Principal - Dashboard")
        # itera sobre las opciones del diccionario opciones.
        for key in opciones:
            # imprime cada opción con su número y ruta correspondiente.
            print(f"{key} - {opciones[key]}")
            # imprime la opción "0 - Salir" para permitir al usuario salir del menú.
        print("0 - Salir")

        # Pide que se ingrese una opcion
        eleccion = input("Elige uno de los siguientes scripts para ver su codigo o '0' para salir: ")
        # Si la eleccion es 0 se rompe el bucle
        if eleccion == '0':
            break

        # Si el usuario ingresa una opción válida
        elif eleccion in opciones:
            # construye la ruta absoluta del script correspondiente utilizando la función os.path.join y la ruta base.
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            # llama a la función mostrar_codigo para mostrar el código del script.
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
# Verifica si el script se está ejecutando directamente (no se está importando como módulo)
if __name__ == "__main__":
    # llama a la función mostrar_menu para iniciar el menú.
    mostrar_menu()