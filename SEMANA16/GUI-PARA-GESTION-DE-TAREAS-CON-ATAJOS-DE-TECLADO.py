import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, texto):
        self.texto = texto
        self.completada = False

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.tareas = []
        self.crear_widgets()

    def crear_widgets(self):
        self.entrada_tarea = tk.Entry(self.root, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=5, pady=5)

        self.boton_anadir = tk.Button(self.root, text="Añadir", command=self.anadir_tarea)
        self.boton_anadir.grid(row=0, column=1, padx=5, pady=5)

        self.lista_tareas = tk.Listbox(self.root, width=40)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.boton_completar = tk.Button(self.root, text="Completar", command=self.completar_tarea)
        self.boton_completar.grid(row=2, column=0, padx=5, pady=5)

        self.boton_eliminar = tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

        self.root.bind("<Return>", self.anadir_tarea_con_enter)
        self.root.bind("c", self.completar_tarea_con_tecla)
        self.root.bind("d", self.eliminar_tarea_con_tecla)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def anadir_tarea(self):
        texto = self.entrada_tarea.get()
        if texto:
            tarea = Tarea(texto)
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, texto)
            self.entrada_tarea.delete(0, tk.END)

    def anadir_tarea_con_enter(self, evento):
        self.anadir_tarea()

    def completar_tarea(self):
        indice = self.lista_tareas.curselection()
        if indice:
            tarea = self.tareas[indice[0]]
            tarea.completada = True
            self.lista_tareas.itemconfig(indice, fg="green")

    def completar_tarea_con_tecla(self, evento):
        self.completar_tarea()

    def eliminar_tarea(self):
        indice = self.lista_tareas.curselection()
        if indice:
            self.tareas.pop(indice[0])
            self.lista_tareas.delete(indice)

    def eliminar_tarea_con_tecla(self, evento):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, evento):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = Aplicacion(root)
    root.mainloop()