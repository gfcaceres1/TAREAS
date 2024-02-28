# Matriz bidimensional de ejemplo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
  """
  Función que busca un valor específico en una matriz bidimensional.

  Parámetros:
    matriz: La matriz bidimensional en la que se realiza la búsqueda.
    valor: El valor que se desea encontrar.



  Retorno:
    Una tupla con la fila y la columna donde se encuentra el valor, o None si no se encuentra.
  """
  for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
      if matriz[fila][columna] == valor:
        return fila, columna
  return None

# Valor a buscar
valor_a_buscar = 5

# Búsqueda del valor
fila, columna = buscar_valor(matriz, valor_a_buscar)

# Impresión del resultado
if fila is None and columna is None:
  print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")
else:
  print(f"El valor {valor_a_buscar} se encuentra en la fila {fila+1} y la columna {columna+1}.")
