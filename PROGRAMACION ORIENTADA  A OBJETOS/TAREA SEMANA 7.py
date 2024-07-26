class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Inicializa los atributos del objeto y abre el archivo.

        :param nombre: Nombre del archivo a gestionar.
        """
        self.nombre = nombre
        self.archivo = None
        try:
            self.archivo = open(nombre, 'w')
            print(f"Archivo '{nombre}' abierto correctamente.")
        except IOError as e:
            print(f"No se pudo abrir el archivo '{nombre}': {e}")

    def escribir(self, contenido):
        """
        Escribe contenido en el archivo.


        :param contenido: Texto a escribir en el archivo.
        """
        if self.archivo:
            try:
                self.archivo.write(contenido)
                print(f"Escribiendo en el archivo '{self.nombre}': {contenido}")
            except IOError as e:
                print(f"No se pudo escribir en el archivo '{self.nombre}': {e}")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo si está abierto y realiza la limpieza necesaria.
        """
        if self.archivo:
            try:
                self.archivo.close()
                print(f"Archivo '{self.nombre}' cerrado correctamente.")
            except IOError as e:
                print(f"No se pudo cerrar el archivo '{self.nombre}': {e}")
        else:
            print(f"No hay archivo '{self.nombre}' para cerrar.")


# Demostración del uso de la clase Archivo
if __name__ == "__main__":
    # Creación de un objeto Archivo
    archivo = Archivo("mi_archivo.txt")

    # Uso del método escribir para escribir en el archivo
    archivo.escribir("Hola, este es un contenido de prueba.")

    # Eliminación explícita del objeto para invocar el destructor
    del archivo

    # Al finalizar el script, si no se ha invocado explícitamente el destructor,
    # Python lo llamará automáticamente cuando el objeto ya no sea necesario.
