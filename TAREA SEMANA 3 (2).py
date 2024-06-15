class RegistroDiario:
  """
  Clase que representa la información diaria del clima.

  Atributos:
    dia (str): Nombre del día de la semana (ej. "Lunes", "Martes").
    temperatura (float): Temperatura registrada para el día.

  Métodos:
    __init__(self, dia): Inicializa el registro diario con el día especificado.
    ingresar_temperatura(self): Solicita al usuario la temperatura del día y la almacena en el atributo correspondiente.
    obtener_temperatura(self): Devuelve la temperatura registrada para el día.
  """

  def __init__(self, dia):
    self.dia = dia
    self.temperatura = None

  def ingresar_temperatura(self):
    """
    Solicita al usuario la temperatura del día y la almacena en el atributo correspondiente.
    """
    self.temperatura = float(input(f"Ingrese la temperatura del {self.dia}: "))

  def obtener_temperatura(self):
    """
    Devuelve la temperatura registrada para el día.
    """
    return self.temperatura

class RegistroSemanal:
  """
  Clase que gestiona un conjunto de registros diarios y calcula el promedio semanal de temperaturas.

  Atributos:
    registros_diarios (list): Lista de objetos `RegistroDiario` que representan los registros de cada día.

  Métodos:
    __init__(self): Inicializa el registro semanal.
    agregar_registro_diario(self, registro_diario): Agrega un registro diario a la lista.
    calcular_promedio_semanal(self): Calcula y devuelve el promedio semanal de temperaturas.
  """

  def __init__(self):
    self.registros_diarios = []

  def agregar_registro_diario(self, registro_diario):
    """
    Agrega un registro diario a la lista.
    """
    self.registros_diarios.append(registro_diario)

  def calcular_promedio_semanal(self):
    """
    Calcula y devuelve el promedio semanal de temperaturas.
    """
    if not self.registros_diarios:
      raise Exception("No hay registros diarios para calcular el promedio")

    temperaturas = [registro.obtener_temperatura() for registro in self.registros_diarios]
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main():
  """
  Función principal del programa.
  """
  registro_semanal = RegistroSemanal()

  # Se crean objetos `RegistroDiario` para cada día de la semana
  dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
  for dia in dias:
    registro_diario = RegistroDiario(dia)
    registro_diario.ingresar_temperatura()
    registro_semanal.agregar_registro_diario(registro_diario)


  # Se calcula y muestra el promedio semanal de temperaturas
  try:
    promedio_semanal = registro_semanal.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es de: {promedio_semanal:.2f}°C")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
