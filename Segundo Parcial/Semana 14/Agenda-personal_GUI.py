# Importamos las bibliotecas necesarias para crear la interfaz gráfica y trabajar con fechas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
import re

# Creamos la ventana principal de la aplicación
api = tk.Tk()
# Establecemos el tamaño de la ventana
api.geometry("1200x700")
# Establecemos el título de la ventana
api.title("Agenda Personal")
# Establecemos el color de fondo de la ventana
api.config(bg="#171e2b")
# Creamos un frame dentro de la ventana para organizar los elementos
frame2 = tk.Frame(api, bg="#242424")
# Establecemos que el frame se expanda para ocupar el espacio disponible
frame2.pack(fill="both", expand=True)
# Creamos un label para mostrar el texto "Fecha del evento:"
label_fecha = tk.Label(frame2, text="Fecha del evento: ", background="#242424", font=("Bauhaus_93", 12), foreground="white")
# Establecemos la posición del label en la ventana
label_fecha.place(x=10, y=10)
# Obtenemos la fecha actual
hoy = date.today()
# Creamos un widget para seleccionar la fecha del evento
fecha = DateEntry(frame2, mindate=hoy)
# Establecemos la posición del widget en la ventana
fecha.place(x=150, y=13)
# Creamos un label para mostrar el texto "Hora del evento:"
tk.Label(frame2, text="Hora del evento: ", background="#242424", font=("Bauhaus_93", 12), foreground="white").place(x=300, y=10)


# Definimos una función para validar la hora ingresada
def validar_hora(hora):
    # Establecemos el patrón para la hora (HH:MM:SS)
    patron = r"^\d{2}:\d{2}:\d{2}$"
    # Devolvemos True si la hora coincide con el patrón, False en caso contrario
    return re.match(patron, hora) is not None


# Definimos una función para obtener la hora ingresada
def obtener_hora():
    # Obtenemos el texto ingresado en el campo de hora
    hora_ingresada = hora.get()
    # Validamos la hora ingresada
    if validar_hora(hora_ingresada):
        # Si la hora es válida, devolvemos el texto ingresado
        return hora_ingresada
    else:
        # Si la hora no es válida, establecemos el foco en el campo de hora
        hora.focus()


# Definimos una función para validar si un texto es un número
def validar_numero(texto):
    # Devolvemos True si el texto es un número, False en caso contrario
    number = (texto.isnumeric())
    return number


# Creamos un campo de texto para ingresar la hora del evento
hora = tk.Entry(api, background="#618a4f")
# Establecemos la posición del campo de texto en la ventana
hora.place(x=430, y=13)
# Creamos un label para mostrar el texto "Descripción del evento:"
tk.Label(frame2, text="Descripción del evento: ", background="#242424", font=("Bauhaus_93", 12), foreground="white").place(x=10, y=50)


# Definimos una función para validar si un texto es una tecla válida (solo letras y espacios)
def validar_tecla(texto):
    # Devolvemos True si el texto es una tecla válida, False en caso contrario
    tecla = (texto.isalpha and texto.isspace)
    return tecla


# Creamos un comando de validación para el campo de descripción
vcmd = (api.register(validar_tecla), '%P')
# Creamos un campo de texto para ingresar la descripción del evento
descripcion = tk.Entry(api, background="#618a4f", width=55)
# Establecemos la posición del campo de texto en la ventana
descripcion.place(x=190, y=53)
# Establecemos la validación para el campo de texto
descripcion.config(validate='key', validatecommand=vcmd)
# Creamos un frame para la lista de eventos
frame1 = tk.Frame(api)
# El frame se expande para ocupar el espacio disponible
frame1.pack(fill="x", expand=True)
# Creamos una lista de eventos
lista_eventos = ttk.Treeview(frame1)
# Establecemos las columnas de la lista de eventos
lista_eventos["columns"] = ("Fecha", "Hora", "Descripción")
# Establecemos el ancho de cada columna
lista_eventos.column("#0", width=0, stretch=tk.NO)
lista_eventos.column("Fecha", anchor=tk.W, width=100)
lista_eventos.column("Hora", anchor=tk.W, width=50)
lista_eventos.column("Descripción", anchor=tk.W, width=200)
# Establecemos los títulos de las columnas
lista_eventos.heading("#0", text="", anchor=tk.W)
lista_eventos.heading("Fecha", text="Fecha", anchor=tk.W)
lista_eventos.heading("Hora", text="Hora", anchor=tk.W)
lista_eventos.heading("Descripción", text="Descripción", anchor=tk.W)
# Establecemos la posición de la lista de eventos en la ventana
lista_eventos.pack(fill="both", expand=True)


# Definimos una función para crear un evento
def crea_evento():
    # Obtenemos la fecha y hora del evento
    date = fecha.get()
    hour = obtener_hora()
    # Obtenemos la descripción del evento
    description = descripcion.get()
    # Verificamos si todos los campos están completos
    if date and hour and description:
        # Agregamos el evento a la lista de eventos
        lista_eventos.insert("", "end", values=(date, hour, description))
        # Limpiamos los campos de texto
        fecha.delete(0, tk.END)
        descripcion.delete(0, tk.END)
        hora.delete(0, tk.END)
        # Habilitamos el botón de eliminar evento
        eliminar.config(state="normal")
    else:
        # Mostramos un mensaje de error si no todos los campos están completos
        messagebox.showerror("Error", "Por favor, complete todos los campos o ingrese bien la hora")
        # Establecemos el foco en el campo de hora
        hora.focus()


# Creamos un botón para agregar un evento
agregar = tk.Button(frame2, text="Agregar Evento", bg="#3c15ad", fg="white", command=crea_evento, activebackground="#ff7f7f", activeforeground="white", borderwidth="1")
# Establecemos la posición del botón en la ventana
agregar.place(x=20, y=100)


# Definimos una función para eliminar un evento
def eliminar_evento():
    # Obtenemos la selección actual en la lista de eventos
    seleccionado = lista_eventos.selection()
    # Verificamos si hay un evento seleccionado
    if seleccionado:
        # Eliminamos el evento seleccionado
        lista_eventos.delete(seleccionado)
    else:
        # Mostramos un mensaje de error si no hay un evento seleccionado
        messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar")


# Creamos un botón para eliminar un evento
eliminar = tk.Button(frame2, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="red", fg="white", activebackground="#3d4078", activeforeground="white", borderwidth="1")
# Establecemos la posición del botón en la ventana
eliminar.place(x=130, y=100)
# Deshabilitamos el botón de eliminar evento por defecto
eliminar.config(state="disabled")
# Creamos un botón para salir de la aplicación
tk.Button(frame2, text="Salir", command=api.destroy, bg="black", fg="white", borderwidth=1).place(x=320, y=100)
# Iniciamos la aplicación
api.mainloop()
