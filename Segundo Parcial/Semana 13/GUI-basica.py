import tkinter as TK
from tkinter import ttk
from tkinter import messagebox
api = TK.Tk()

api.geometry("800x400")
api.configure(background= "#1e1e1e")
TK.Wm.wm_title(api, "Aplicación GUI")
nombre = TK.Entry(api, bg="#7f747e", fg="white")
apellido = TK.Entry(api, bg="#030614", fg="white")
man = TK.BooleanVar()
woman = TK.BooleanVar()
man.set(False)
woman.set(False)
def habilita_click():
    nombre.config(state="normal")
    nombre.delete(0, TK.END)
    nombre.focus()
    apellido.config(state="normal")
    apellido.delete(0,TK.END)
    man.set(False)
    man_checkbox.config(state="active")
    woman.set(False)
    woman_checkbox.config(state="active")
    agregar.config(state="active")
    habilita.config(state="disabled")

habilita =TK.Button(api, text="habilitar", command=habilita_click,font=("Consolas", 12), bg="#202a54", fg="#ce9178",relief="flat", activebackground= "#3d4078", activeforeground= "white", borderwidth="0")
habilita.place(x=80, y= 200)
habilita.config(state="disabled")
def limpiar_lista():
        
        if listbox.size() == 0:
            messagebox.showerror("Error", "La lista está vacía.")
            return
        listbox.delete(0, TK.END)

def agrega_datos():
     name = nombre.get()
     surname = apellido.get()
     gender = obtener_genero()
     if name != "":
        if surname!= "":
            if gender != "x":
                nombre.config(state="disabled")
                apellido.config(state="disabled")
                man_checkbox.config(state="disabled")
                woman_checkbox.config(state="disabled")
                habilita.config(state="active")
                habilita.place(x=80, y= 200)
                agregar.config(state="disabled")
                listbox.insert(TK.END, "Nombre: " + name)
                listbox.insert(TK.END, "Apellido: " + surname)
                listbox.insert(TK.END, "Género: " + gender)
            else:
                messagebox.showerror("Error", "Seleccione un género")
                man_checkbox.focus()
        else:
            messagebox.showerror("Error", "Ingrese su apellido")
            apellido.focus()
     else:
        messagebox.showerror("Error", "Ingrese su nombre")
        nombre.focus()



def obtener_genero():
    obtener_genero = str(man.get and woman.get)
    if not obtener_genero == "":
        return "masculino"
    elif not obtener_genero == "":
        return "femenino"
    else:
        return "x"

TK.Label(api, text="Ingrese su nombre:", font=("Courier"), bg="#1e1e1e", fg="#e4ab22").place(x=10, y= 10)
nombre.place(x=230, y=15)

TK.Label(api, text="Ingrese su apellido:", font=("Courier"), bg="#1e1e1e", fg="#e4ab22").place(x=10, y=50)
apellido.place(x=230, y=54)

TK.Label(api, text="Seleccione su genero:", font=("Courier"), bg="#1e1e1e", fg="#e4ab22").place(x=10, y=100)

man_checkbox=TK.Radiobutton(api, text="Masculino", value="Masculino", variable= man, width="8", background="#006450")
man_checkbox.place(x=230, y=91)
woman_checkbox = TK.Radiobutton(api, text="Femenino", value="f", variable=woman, width="8", background="#d77246")
woman_checkbox.place(x=230, y=115)
agregar = TK.Button(api, text="Añadir", font=("Consolas", 12), bg="#202a54", fg="#ce9178",relief="flat", activebackground= "#3d4078", activeforeground= "white", borderwidth="0", command= agrega_datos)
agregar.place(x=10, y=200)
TK.Button(api, text="Salir", command=api.quit, font=("Consolas", 12), bg="#202a54", fg="#ce9178",relief="flat", activebackground= "#3d4078", activeforeground= "white", borderwidth="0").place(x=190, y=200)


listbox = TK.Listbox(api,background="#7cff07")
listbox.place(x=500, y=10)

borrar_lista = TK.Button(api, text="Borrar Lista", command= limpiar_lista, bg="#202a54", fg="#ce9178",relief="flat", activebackground= "#3d4078", activeforeground= "white", borderwidth="0")
borrar_lista.place(x=530, y= 200)

api.mainloop()