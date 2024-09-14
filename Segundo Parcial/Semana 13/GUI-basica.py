# Importar el m ódulo tkinter y asignarle el alias TK
import tkinter as TK

# Importar el módulo ttk desde tkinter
from tkinter import ttk

# Importar el módulo messagebox desde tkinter
from tkinter import messagebox

# Crear una nueva ventana de aplicación tkinter
api = TK.Tk()

# Establecer la geometría de la ventana de aplicación a 800x400 píxeles
api.geometry("800x400")

# Establecer el color de fondo de la ventana de aplicación a #1e1e1e
api.configure(background= "#1e1e1e")

# Establecer el título de la ventana de aplicación a "Aplicación GUI"
TK.Wm.wm_title(api, "Aplicación GUI")

# Crear un widget Entry para el nombre del usuario
nombre = TK.Entry(api, bg="#7f747e", fg="white")

# Crear un widget Entry para el apellido del usuario
apellido = TK.Entry(api, bg="#030614", fg="white")

# Crear dos variables BooleanVar para almacenar la selección de género del usuario
man = TK.BooleanVar()
woman = TK.BooleanVar()

# Establecer los valores iniciales de las variables BooleanVar a Falso
man.set(False)
woman.set(False)

# Definir una función para habilitar los widgets Entry y casillas de verificación
def habilita_click():
    # Habilitar el widget Entry nombre y borrar su contenido
    nombre.config(state="normal")
    nombre.delete(0, TK.END)
    nombre.focus()
    
    # Habilitar el widget Entry apellido y borrar su contenido
    apellido.config(state="normal")
    apellido.delete(0,TK.END)
    
    # Establecer la variable BooleanVar man a Falso
    man.set(False)
    
    # Habilitar la casilla de verificación man
    man_checkbox.config(state="active")
    
    # Establecer la variable BooleanVar woman a Falso
    woman.set(False)
    
    # Habilitar la casilla de verificación woman
    woman_checkbox.config(state="active")
    
    # Habilitar el botón agregar
    agregar.config(state="active")
    
    # Deshabilitar el botón habilita
    habilita.config(state="disabled")

# Crear un botón para habilitar los widgets Entry y casillas de verificación
habilita = TK.Button(api, text="habilitar", command=habilita_click, 
                     font=("Consolas", 12), bg="#202a54", fg="#ce9178", 
                     relief="flat", activebackground= "#3d4078", 
                     activeforeground= "white", borderwidth="0")

# Colocar el botón habilita en la posición (80, 200)
habilita.place(x=80, y= 200)

# Deshabilitar el botón habilita inicialmente
habilita.config(state="disabled")

# Definir una función para limpiar la lista
def limpiar_lista():
    # Verificar si la lista está vacía
    if listbox.size() == 0:
        # Mostrar un mensaje de error si la lista está vacía
        messagebox.showerror("Error", "La lista está vacía.")
        return
    
    # Borrar el contenido de la lista
    listbox.delete(0, TK.END)

# Definir una función para agregar datos a la lista
def agrega_datos():
    # Obtener el nombre y apellido del usuario desde los widgets Entry
    name = nombre.get()
    surname = apellido.get()
    
    # Obtener la selección de género del usuario
    gender = obtener_genero()
    
    # Verificar si el usuario ha ingresado su nombre y apellido
    if name != "":
        if surname!= "":
            # Verificar si el usuario ha seleccionado un género
            if gender != "x":
                # Deshabilitar los widgets Entry y casillas de verificación
                nombre.config(state="disabled")
                apellido.config(state="disabled")
                man_checkbox.config(state="disabled")
                woman_checkbox.config(state="disabled")
                
                # Habilitar el botón habilita
                habilita.config(state="active")
                habilita.place(x=80, y= 200)
                
                # Deshabilitar el botón agregar
                agregar.config(state="disabled")
                
                # Agregar los datos del usuario a la lista
                listbox.insert(TK.END, "Nombre: " + name)
                listbox.insert(TK.END, "Apellido: " + surname)
                listbox.insert(TK.END, "Género: " + gender)
            else:
                # Mostrar un mensaje de error si el usuario no ha seleccionado un género
                messagebox.showerror("Error", "Seleccione un género")
                man_checkbox.focus()
        else:
            # Mostrar un mensaje de error si el usuario no ha ingresado su apellido
            messagebox.showerror("Error", "Ingrese su apellido")
            apellido.focus()
    else:
        # Mostrar un mensaje de error si el usuario no ha ingresado su nombre
        messagebox.showerror("Error", "Ingrese su nombre")
        nombre.focus()

# Definir una función para obtener la selección de género del usuario
def obtener_genero():
    # Obtener los valores de las variables BooleanVar man y woman
    obtener_genero = str(man.get() and woman.get)
    
    # Verificar si el usuario ha seleccionado un género
    if not obtener_genero == "":
        return "masculino"
    elif not obtener_genero == "":
        return "femenino"
    else:
        return "x"

# Crear una etiqueta para solicitar al usuario que ingrese su nombre
TK.Label(api, text="Ingrese su nombre:", font=("Courier"), bg="#1e1e1e", fg="#e4ab22").place(x=10, y= 10)

# Colocar el widget Entry nombre en la posición (230, 15)
nombre.place(x=230, y=15)

# Crear una etiqueta para solicitar al usuario que ingrese su apellido
TK.Label(api, text="Ingrese su apellido:", font=("Courier"), bg="#1e1e1e", fg="#e4ab22").place(x=10, y=50)

# Colocar el widget Entry apellido en la posición (230, 54)
apellido.place(x=230, y=54)

# Crear una etiqueta para solicitar al usuario que seleccione su género
TK.Label(api, text="Seleccione su género:", font=("Courier"), bg="#1e1e1e", fg="#e4ab22").place(x=10, y=100)

# Crear una casilla de verificación para que el usuario seleccione "Masculino"
man_checkbox=TK.Radiobutton(api, text="Masculino", value="Masculino", variable= man, width="8", background="#006450")
man_checkbox.place(x=230, y=91)

# Crear una casilla de verificación para que el usuario seleccione "Femenino"
woman_checkbox = TK.Radiobutton(api, text="Femenino", value="f", variable=woman, width="8", background="#d77246")
woman_checkbox.place(x=230, y=115)

# Crear un botón para agregar datos a la lista
agregar = TK.Button(api, text="Añadir", font=("Consolas", 12), bg="#202a54", fg="#ce9178", 
                     relief="flat", activebackground= "#3d4078", activeforeground= "white", 
                     borderwidth="0", command= agrega_datos)

# Colocar el botón agregar en la posición (10, 200)
agregar.place(x=10, y=200)

# Crear un botón para salir de la aplicación
TK.Button(api, text="Salir", command=api.quit, font=("Consolas", 12), bg="#202a54", fg="#ce9178", 
          relief="flat", activebackground= "#3d4078", activeforeground= "white", borderwidth="0").place(x=190, y=200)

# Crear una lista para mostrar los datos del usuario
listbox = TK.Listbox(api,background="#7cff07")
listbox.place(x=500, y=10)

# Crear un botón para borrar la lista
borrar_lista = TK.Button(api, text="Borrar Lista", command= limpiar_lista, bg="#202a54", fg="#ce9178", 
                          relief="flat", activebackground= "#3d4078", activeforeground= "white", borderwidth="0")
borrar_lista.place(x=530, y= 200)

# Iniciar la ventana de aplicación
api.mainloop()