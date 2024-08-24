import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def agregar_producto(self, codigo, nombre, precio):
        self.productos[codigo] = {"nombre": nombre, "precio": precio}
        self.guardar_inventario()
        print("Producto agregado exitosamente al inventario.")

    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio):
        if codigo in self.productos:
            self.productos[codigo]["nombre"] = nuevo_nombre
            self.productos[codigo]["precio"] = nuevo_precio
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")


    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as archivo:
                self.productos = json.load(archivo)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al cargar el inventario. El archivo puede estar dañado.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as archivo:
                json.dump(self.productos, archivo)
        except PermissionError:
            print("No se tienen permisos para escribir en el archivo.")

if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(codigo, nombre, precio)
        elif opcion == "2":
            codigo = input("Ingrese el código del producto a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_producto(codigo, nuevo_nombre, nuevo_precio)
        elif opcion == "3":
            codigo = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
