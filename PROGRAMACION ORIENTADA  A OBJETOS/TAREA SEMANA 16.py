import tkinter as tk

class ListaTareas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Tareas")
        self.geometry("300x400")

        # Variables
        self.tareas = []
        self.tarea_actual = None

        # Elementos de la interfaz
        self.entrada_tarea = tk.Entry(self)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.bind("<Return>", self.agregar_tarea)

        self.lista_tareas = tk.Listbox(self)
        self.lista_tareas.pack(fill=tk.BOTH, expand=True)
        self.lista_tareas.bind("<Double-Button-1>", self.marcar_completada)
        self.lista_tareas.bind("<Delete>", self.eliminar_tarea)

        # Botones
        boton_agregar = tk.Button(self, text="Agregar", command=self.agregar_tarea)
        boton_agregar.pack()
        boton_marcar = tk.Button(self, text="Marcar Completada", command=self.marcar_completada)
        boton_marcar.pack()
        boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_tarea)
        boton_eliminar.pack()

        # Atajos de teclado
        self.bind("<Control-c>", self.marcar_completada)
        self.bind("<Escape>", self.quit)

    def agregar_tarea(self, event=None):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)

    def marcar_completada(self, event=None):
        indice = self.lista_tareas.curselection()
        if indice:
            tarea = self.tareas[indice[0]]
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, f"✅ {tarea}")
            self.tareas[indice[0]] = f"✅ {tarea}"

    def eliminar_tarea(self, event=None):
        indice = self.lista_tareas.curselection()
        if indice:
            self.lista_tareas.delete(indice)
            del self.tareas[indice[0]]

if __name__ == "__main__":
    app = ListaTareas()
    app.mainloop()
