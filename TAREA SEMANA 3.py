def ingresar_temperatura_dia(dia):
  """
  Función para ingresar la temperatura de un día específico.

  Parámetros:
    dia (str): Nombre del día de la semana (ej. "Lunes", "Martes").

  Retorno:
    float: Temperatura ingresada por el usuario para el día especificado.
  """
  temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
  return temperatura

def calcular_promedio_semanal(temperaturas):
  """
  Función para calcular el promedio semanal de temperaturas.

  Parámetros:
    temperaturas (list): Lista de temperaturas diarias.

  Retorno:
    float: Promedio semanal de temperaturas.
  """
  promedio = sum(temperaturas) / len(temperaturas)
  return promedio


def main():
  """
  Función principal del programa.
  """
  # Se inicializa una lista vacía para almacenar las temperaturas diarias
  temperaturas_semanales = []

  # Se ingresan las temperaturas para cada día de la semana
  for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
    temperatura_dia = ingresar_temperatura_dia(dia)
    temperaturas_semanales.append(temperatura_dia)

  # Se calcula y muestra el promedio semanal de temperaturas
  promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
  print(f"El promedio semanal de temperaturas es de: {promedio_semanal:.2f}°C")

if __name__ == "__main__":
  main()
