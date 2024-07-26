import os
import subprocess

def mostrar_codigo(ruta_script):
  """
  Función para mostrar el código de un script Python específico.

  Args:
    ruta_script (str): Ruta absoluta del script Python.

  Returns:
    str: Código del script Python, o None si ocurre un error.
  """
  ruta_script_absoluta = os.path.abspath(ruta_script)
  try:
    with open(ruta_script_absoluta, 'r') as archivo:
      codigo = archivo.read()
      print(f"\n--- Código de {ruta_script} ---\n")
      print(codigo)
      return codigo
  except FileNotFoundError:
    print("El archivo no se encontró.")
    return None
  except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    return None

def ejecutar_codigo(ruta_script):
  """
  Función para ejecutar un script Python específico.

  Args:
    ruta_script (str): Ruta absoluta del script Python.
  """
  try:
    if os.name == 'nt':  # Windows
      subprocess.Popen(['cmd', '/k', 'python', ruta_script])
    else:  # Sistemas basados en Unix
      subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
  except Exception as e:
    print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_scripts_especificos():
  """
  Función para mostrar y permitir la interacción con scripts Python específicos.

  Los nombres de los scripts deben ser "TAREA SEMANA 4.py", "TAREA SEMANA 5.py" y "TAREA SEMANA 6.py".
  """
  # Obtiene la ruta actual del directorio de trabajo
  ruta_actual = os.getcwd()

  # Lista los scripts Python en la ruta actual
  scripts_disponibles = [f for f in os.listdir(ruta_actual) if f.endswith('.py')]

  # Filtra los scripts con los nombres específicos
  scripts_filtrados = [s for s in scripts_disponibles if s in ["TAREA SEMANA 4.py", "TAREA SEMANA 5.py", "TAREA SEMANA 6.py"]]

  if not scripts_filtrados:
    print("No se encontraron scripts Python con los nombres especificados.")
    return

  while True:
    print("\nScripts - Selecciona un script para ver y ejecutar")
    for i, script in enumerate(scripts_filtrados, start=1):
      print(f"{i} - {script}")
    print("0 - Regresar al menú principal")

    eleccion_script = input("Elige un script o '0' para regresar: ")
    if eleccion_script == '0':
      break
    else:
      try:
        eleccion_script = int(eleccion_script) - 1
        if 0 <= eleccion_script < len(scripts_filtrados):
          ruta_script = os.path.join(ruta_actual, scripts_filtrados[eleccion_script])
          codigo = mostrar_codigo(ruta_script)
          if codigo:
            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
            if ejecutar == '1':
              ejecutar_codigo(ruta_script)
            elif ejecutar == '0':
              print("No se ejecutó el script.")
            else:
              print("Opción no válida. Regresando al menú de scripts.")
            input("\nPresiona Enter para volver al menú de scripts.")
        else:
          print("Opción no válida. Por favor, intenta de nuevo.")
      except ValueError:
        print("Opción no válida. Por favor, intenta de nuevo.")
