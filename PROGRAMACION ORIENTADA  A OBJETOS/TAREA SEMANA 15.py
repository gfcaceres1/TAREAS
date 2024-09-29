import tkinter as tk

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Tareas")

        # Crear los elementos de la interfaz
        self.entry_task = tk.Entry(master)
        self.entry_task.pack()

        self.button_add = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.button_add.pack()

        self.button_complete = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.button_complete.pack()

        self.button_delete = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.button_delete.pack()

        self.task_list = tk.Listbox(master)
        self.task_list.pack()

        # Lista para almacenar las tareas
        self.tasks = []

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_task = self.task_list.get(selected_index)
            self.task_list.delete(selected_index)
            self.tasks.remove(selected_task)
            # Puedes agregar aquí lógica para marcar la tarea como completada en algún almacenamiento persistente

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
            del self.tasks[selected_index]

# Crear la ventana principal y la instancia de la aplicación
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
