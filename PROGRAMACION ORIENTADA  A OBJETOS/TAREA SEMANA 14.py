import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de eventos (simulada)
        self.eventos = []

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(fill="both", expand=True)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("fecha", "hora", "descripcion"))
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # Frame para los campos de entrada y botones
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(fill="x")

        # Labels y campos de entrada
        self.label_fecha = ttk.Label(self.frame_entrada, text="Fecha:")
        self.label_fecha.pack(side="left")
        self.entry_fecha = ttk.Entry(self.frame_entrada)
        self.entry_fecha.pack(side="left")

        self.label_hora = ttk.Label(self.frame_entrada, text="Hora:")
        self.label_hora.pack(side="left")
        self.entry_hora = ttk.Entry(self.frame_entrada)
        self.entry_hora.pack(side="left")

        self.label_descripcion = ttk.Label(self.frame_entrada, text="Descripción:")
        self.label_descripcion.pack(side="left")
        self.entry_descripcion = ttk.Entry(self.frame_entrada)
        self.entry_descripcion.pack(fill="x")

        # Botones
        self.btn_agregar = ttk.Button(self.frame_entrada, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side="right", padx=10)
        self.btn_eliminar = ttk.Button(self.frame_entrada, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.pack(side="right")

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()
        self.eventos.append((fecha, hora, descripcion))
        self.actualizar_lista()
        self.limpiar_campos()

    def eliminar_evento(self):
        item_seleccionado = self.tree.selection()
        if item_seleccionado:
            if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento?"):
                self.eventos.pop(self.tree.index(item_seleccionado))
                self.actualizar_lista()

    def actualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for evento in self.eventos:
            self.tree.insert("", "end", values=evento)

    def limpiar_campos(self):
        self.entry_fecha.delete(0, "end")
        self.entry_hora.delete(0, "end")
        self.entry_descripcion.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
