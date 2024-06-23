
# Clase base para representar a una persona
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def __str__(self):
        return f'Nombre: {self.__nombre}, Edad: {self.__edad}'


# Clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, edad, cliente_id):
        super().__init__(nombre, edad)
        self.__cliente_id = cliente_id

    def get_cliente_id(self):
        return self.__cliente_id

    def __str__(self):
        return f'Cliente ID: {self.__cliente_id}, {super().__str__()}'


# Clase Empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, empleado_id):
        super().__init__(nombre, edad)
        self.__empleado_id = empleado_id

    def get_empleado_id(self):
        return self.__empleado_id

    def __str__(self):
        return f'Empleado ID: {self.__empleado_id}, {super().__str__()}'


# Clase para representar un producto
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def __str__(self):
        return f'Producto: {self.__nombre}, Precio: {self.__precio}'


# Clase para representar un pedido
class Pedido:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def get_total(self):
        return sum(producto.get_precio() for producto in self.__productos)

    def __str__(self):
        productos_str = '\n'.join(str(producto) for producto in self.__productos)
        return f'Pedido de {self.__cliente.get_nombre()}:\n{productos_str}\nTotal: {self.get_total()}'


# Ejemplo de uso
def main():
    # Crear algunos productos
    producto1 = Producto('Laptop', 1500)
    producto2 = Producto('Mouse', 20)
    producto3 = Producto('Teclado', 30)

    # Crear un cliente
    cliente1 = Cliente('Juan Pérez', 30, 'C001')

    # Crear un pedido para el cliente
    pedido1 = Pedido(cliente1)
    pedido1.agregar_producto(producto1)
    pedido1.agregar_producto(producto2)
    pedido1.agregar_producto(producto3)

    # Imprimir detalles del pedido
    print(pedido1)



if __name__ == '__main__':
    main()

