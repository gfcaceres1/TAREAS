# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca del vehículo: {self.marca}, Modelo: {self.modelo}")

    def arrancar_motor(self):
        print("Arrancando el motor del vehículo...")


# Clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.__puertas = puertas  # Atributo encapsulado

    def mostrar_info(self):
        super().mostrar_info()  # Llamada al método de la clase base
        print(f"Número de puertas: {self.__puertas}")

    def arrancar_motor(self):
        print("Arrancando el motor del coche con una llave...")

    # Método para acceder al atributo encapsulado
    def obtener_puertas(self):
        return self.__puertas

    # Método para modificar el atributo encapsulado
    def establecer_puertas(self, puertas):
        if puertas > 0:
            self.__puertas = puertas
        else:
            print("El número de puertas debe ser positivo.")


# Ejemplo de polimorfismo
class CocheElectrico(Coche):
    def arrancar_motor(self):
        print("Arrancando el motor del coche eléctrico en silencio...")


# Crear instancias de las clases y demostrar funcionalidad
def main():
    vehiculo = Vehiculo("Marca Genérica", "Modelo Genérico")
    vehiculo.mostrar_info()
    vehiculo.arrancar_motor()

    print("\n---\n")

    coche = Coche("Toyota", "Corolla", 4)
    coche.mostrar_info()
    coche.arrancar_motor()

    print("\n---\n")

    coche_electrico = CocheElectrico("Tesla", "Model S", 4)
    coche_electrico.mostrar_info()
    coche_electrico.arrancar_motor()

    print("\n---\n")

    # Encapsulación: modificar y acceder al atributo privado
    coche.establecer_puertas(2)
    print(f"Número de puertas actualizado: {coche.obtener_puertas()}")




if __name__ == "__main__":
    main()
