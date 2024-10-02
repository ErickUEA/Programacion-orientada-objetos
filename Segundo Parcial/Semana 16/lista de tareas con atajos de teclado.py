from tkinter import *
import messagebox
api = Tk()
api.geometry("700x700")
api.configure(bg="#1e1f22")
api.title("Lista de Tareas")
tareas = []
tareas_completadas = set()


def agrega_tarea():
    task = tarea.get()
    if task != "":
        if task not in tareas_completadas and task not in tareas:
            completar_tarea.config(state="active")
            borrar_tarea.config(state="active")
            estado = " por realizar"
            tareas.append(task)
            Lista.insert(END, f"tarea '{task}' {estado}")
            tarea.delete(0, END)
        else:
            messagebox.showerror("Error", "La tarea ya fue completada o ya existe")
            tarea.focus()
    else:
        messagebox.showerror("Error", "Ingrese una tarea")
        tarea.focus()


def tarea_hecha():
    seleccion = Lista.curselection()
    if seleccion:
        tarea = tareas[seleccion[0]]
        if "completa" in tarea:
            Lista.selection_clear(seleccion[0])
        else:
            estado = "completa"
            tareas[seleccion[0]] = f"tarea '{tarea}' {estado}"
            Lista.delete(seleccion[0])
            Lista.insert(seleccion[0], tareas[seleccion[0]])
            Lista.itemconfig(seleccion[0], fg="#808080")
            tareas_completadas.add(tarea)


def atajo_tarea_hecha(event):  # Función que se ejecuta al hacer doble clic en una tarea
    seleccion = Lista.curselection()
    if seleccion:
        tarea = tareas[seleccion[0]]
        if "completa" in tarea:
            Lista.selection_clear(seleccion[0])
        else:
            estado = "completa"
            tareas[seleccion[0]] = f"tarea '{tarea}' {estado}"
            Lista.delete(seleccion[0])
            Lista.insert(seleccion[0], tareas[seleccion[0]])
            Lista.itemconfig(seleccion[0], fg="#808080")
            tareas_completadas.add(tarea)


def elimina_tarea():
    seleccion = Lista.curselection()
    if seleccion:
        task = tareas[seleccion[0]]
        if "completa" in task:
            tareas_completadas.discard(task.split("'")[1])
            tareas.pop(seleccion[0])
            Lista.delete(seleccion[0])
        elif (messagebox.askyesno("", "La tarea no se ha completado desea eliminarla")) == YES:
            tareas.pop(seleccion[0])
            Lista.delete(seleccion[0])
            tareas_completadas.discard(task)
    else:
        Lista.focus()
        messagebox.showerror("Error", "Seleccione la tarea a eliminar")


def atajo_elimina_tarea(event):  # Función que se ejecuta al presionar la tecla Suprimir o Alt+Suprimir
    seleccion = Lista.curselection()
    if seleccion:
        task = tareas[seleccion[0]]
        if "completa" in task:
            tareas_completadas.discard(task.split("'")[1])
            tareas.pop(seleccion[0])
            Lista.delete(seleccion[0])
        elif (messagebox.askyesno("", "La tarea no se ha completado desea eliminarla")) == YES:
            tareas.pop(seleccion[0])
            Lista.delete(seleccion[0])
    else:
        Lista.focus()
        messagebox.showerror("Error", "Seleccione la tarea a eliminar")


Label(api, text="Ingrese la tarea que desea añadir", fg="white", bg="#1e1f22").pack(pady=10)
tarea = Entry(api)
tarea.pack()
tarea.bind("<Return>", lambda event: agrega_tarea())  # Ejecuta la función agrega_tarea al presionar la tecla Enter
agregar_tarea = Button(api, text="Añadir tarea", relief="flat", command=agrega_tarea, overrelief="solid")
agregar_tarea.pack(pady=10)
completar_tarea = Button(api, text="Marcar tarea como completada", overrelief="flat", command=tarea_hecha)
completar_tarea.config(state="disabled")
completar_tarea.pack(pady=5)
borrar_tarea = Button(api, text="Eliminar Tarea", relief="flat", overrelief="sunken", command=elimina_tarea)
borrar_tarea.config(state="disabled")
borrar_tarea.pack(pady=5, padx=10)
Lista = Listbox(api, width=40, height=10)
Lista.pack(pady=10)
scrollbar = Scrollbar(api, orient=VERTICAL, command=Lista.yview)
scrollbar.pack()
Lista.config(yscrollcommand=scrollbar.set)
Lista.bind("<Double-Button-1>", atajo_tarea_hecha)  # Ejecuta la función atajo_tarea_hecha al hacer doble clic en una tarea
Lista.bind("<Delete>", atajo_elimina_tarea)  # Ejecuta la función atajo_elimina_tarea al presionar la tecla Suprimir
api.bind("<Escape>", lambda x: api.destroy())  # Cierra la aplicación al presionar la tecla Escape
api.bind("<Alt-Delete>", atajo_elimina_tarea)  # Ejecuta la función atajo_elimina_tarea al presionar la tecla Alt+Suprimir
api.mainloop()
