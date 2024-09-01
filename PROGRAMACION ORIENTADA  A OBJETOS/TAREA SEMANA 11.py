import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters para los atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        del self.productos[id]

    def actualizar_producto(self, id, nueva_cantidad, nuevo_precio):
        if id in self.productos:
            self.productos[id].set_cantidad(nueva_cantidad)
            self.productos[id].set_precio(nuevo_precio)
        else:
            print("Producto no encontrado")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto.id, producto.nombre, producto.cantidad, producto.precio)

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto.id, producto.nombre, producto.cantidad, producto.precio)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.productos = json.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado")

# Crear instancia de Inventario
inventario = Inventario()

# Cargar inventario desde archivo (si existe)
inventario.cargar_inventario("inventario.json")

# Menú interactivo
while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        id = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        producto = Producto(id, nombre, cantidad, precio)
        inventario.agregar_producto(producto)
    elif opcion == '2':
        id = input("Ingrese el ID del producto a eliminar: ")
        inventario.eliminar_producto(id)
    elif opcion == '3':
        id = input("Ingrese el ID del producto a actualizar: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)
    elif opcion == '4':
        nombre = input("Ingrese el nombre del producto a buscar: ")
        inventario.buscar_producto(nombre)
    elif opcion == '5':
        inventario.mostrar_todos_los_productos()
    elif opcion == '6':
        inventario.guardar_inventario("inventario.json")
    elif opcion == '7':
        break
    else:
        print("Opción inválida")
