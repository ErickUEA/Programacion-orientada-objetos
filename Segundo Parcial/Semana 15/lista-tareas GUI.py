# Importamos la biblioteca tkinter para crear la interfaz gráfica
from tkinter import *
# Importamos la biblioteca messagebox para mostrar mensajes de error
import messagebox
# Creamos una ventana principal llamada "api" con un tamaño de 700x700 píxeles
api = Tk()
api.geometry("700x700")
# Configuramos el color de fondo de la ventana a un gris oscuro
api.config(bg="#1e1f22")
# Establecemos el título de la ventana a "Lista de Tareas"
api.title("Lista de Tareas")
# Creamos dos listas vacías para almacenar las tareas y las tareas completadas
tareas = []
tareas_completas = set()
# Creamos un label para mostrar el texto "Tarea a añadir"
Label(api, text="Tarea a añadir", fg="white", bg="#1e1f22").grid(row=0, column=0, padx=10, pady=10)
# Creamos un campo de entrada para que el usuario ingrese la tarea
tarea = Entry(api, width=23)
tarea.grid(row=0, column=1, padx=0, pady=5)
# Asociamos la función "agrega_tarea" al evento de presionar la tecla "Enter" en el campo de entrada
tarea.bind("<Return>", lambda event: agrega_tarea())


# Definimos la función "agrega_tarea" para agregar una tarea a la lista
def agrega_tarea():
    # Obtenemos el texto ingresado en el campo de entrada
    work = tarea.get()
    # Verificamos si el texto no está vacío
    if work != "":
        # Verificamos si la tarea no ha sido completada anteriormente
        if work not in tareas_completas:
            # Activamos los botones para marcar la tarea como completada y eliminarla
            tarea_completa.config(state="active")
            elimina_tarea.config(state="active")
            # Agregamos la tarea a la lista con el estado "por realizar"
            estado = " por realizar"
            tareas.append(work)
            lista.insert(END, f"tarea '{work}' {estado}")
            # Limpiamos el campo de entrada
            tarea.delete(0, END)
        else:
            # Mostramos un mensaje de error si la tarea ya ha sido completada
            messagebox.showerror("Error", "La tarea ya fue completada")
            tarea.focus()
    else:
        # Mostramos un mensaje de error si el texto está vacío
        messagebox.showerror("Error", "Ingrese una tarea valida")
        tarea.focus()


# Creamos un botón para agregar la tarea a la lista
agrega = Button(api, text="Agregar Tarea", relief="flat", command=agrega_tarea, overrelief="solid")
agrega.grid(row=1, column=0, padx=10, pady=5, columnspan=1)


# Definimos la función "completar_tarea" para marcar una tarea como completada
def completar_tarea():
    # Obtenemos la tarea seleccionada en la lista
    seleccion = lista.curselection()
    # Verificamos si se ha seleccionado una tarea
    if seleccion:
        # Obtenemos la tarea seleccionada
        tarea = tareas[seleccion[0]]
        # Verificamos si la tarea ya ha sido completada
        if "completada" in tarea:
            # Limpiamos la selección si la tarea ya ha sido completada
            lista.selection_clear(seleccion[0])
        else:
            # Marcamos la tarea como completada
            estado = "completada"
            tareas[seleccion[0]] = f"tarea '{tarea}' {estado}"
            lista.delete(seleccion[0])
            lista.insert(seleccion[0], tareas[seleccion[0]])
            lista.itemconfig(seleccion[0], fg="#808080")
            tareas_completas.add(tarea)


# Creamos un botón para marcar la tarea como completada
tarea_completa = Button(api, text="Marcar tarea como completada", overrelief="flat", command=completar_tarea)
tarea_completa.config(state="disabled")
tarea_completa.grid(row=3, column=0, pady=10, padx=10, columnspan=2)


# Definimos la función "eliminar_tarea" para eliminar una tarea de la lista
def eliminar_tarea():
    # Obtenemos la tarea seleccionada en la lista
    seleccion = lista.curselection()
    # Verificamos si se ha seleccionado una tarea
    if seleccion:
        # Obtenemos la tarea seleccionada
        task = tareas[seleccion[0]]
        # Verificamos si la tarea ha sido completada
        if "completada" in task:
            # Eliminamos la tarea de la lista si ha sido completada
            tareas.pop(seleccion[0])
            lista.delete(seleccion[0])
        elif (messagebox.askyesno("", "La tarea no se ha completado desea eliminarla")) == YES:
            # Eliminamos la tarea de la lista si el usuario confirma
            tareas.pop(seleccion[0])
            lista.delete(seleccion[0])
    else:
        # Mostramos un mensaje de error si no se ha seleccionado una tarea
        lista.focus()
        messagebox.showerror("Error", "Seleccione la tarea a eliminar")


# Creamos un botón para eliminar la tarea de la lista
elimina_tarea = Button(api, text="Eliminar Tarea", relief="flat", overrelief="sunken", command=eliminar_tarea)
elimina_tarea.config(state="disabled")
elimina_tarea.grid(row=1, column=1)
# Creamos una lista para mostrar las tareas
lista = Listbox(api, width=40, height=15)
lista.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
# Creamos una barra de desplazamiento para la lista
scrollbar = Scrollbar(api, orient=VERTICAL, command=lista.yview)
scrollbar.grid(row=2, column=3, sticky=NS)
# Configuramos la lista para que se desplace con la barra de desplazamiento
lista.config(yscrollcommand=scrollbar.set)
# Iniciamos la ventana principal
api.mainloop()