import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación GUI")

# Crear los elementos de la interfaz
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=lambda: agregar_dato())
boton_agregar.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=lambda: limpiar_lista())
boton_limpiar.pack()

lista_datos = tk.Listbox(ventana)
lista_datos.pack()

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()
    lista_datos.insert(tk.END, dato)
    entrada.delete(0, tk.END)

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
