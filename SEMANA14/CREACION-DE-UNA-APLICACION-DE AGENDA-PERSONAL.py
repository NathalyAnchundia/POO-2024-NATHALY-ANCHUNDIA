import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

class PersonalAgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.create_widgets()

    def create_widgets(self):
        # Frame para entrada de datos
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # Etiquetas y campos de entrada
        self.date_label = tk.Label(self.input_frame, text="Fecha:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.input_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.input_frame, text="Hora:")
        self.time_label.grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.input_frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        self.description_label = tk.Label(self.input_frame, text="Descripción:")
        self.description_label.grid(row=2, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.input_frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        self.add_button = tk.Button(self.input_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)
        self.delete_button = tk.Button(self.input_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=3, column=1, padx=5, pady=5)
        self.exit_button = tk.Button(self.input_frame, text="Salir", command=self.root.quit)
        self.exit_button.grid(row=3, column=2, padx=5, pady=5)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.root, columns=("date", "time", "description"), show="headings")
        self.tree.heading("date", text="Fecha")
        self.tree.heading("time", text="Hora")
        self.tree.heading("description", text="Descripción")
        self.tree.pack(pady=10)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_entry.get()
        if date and time and description:
            self.tree.insert("", "end", values=(date, time, description))
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            if messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?"):
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalAgendaApp(root)
    root.mainloop()