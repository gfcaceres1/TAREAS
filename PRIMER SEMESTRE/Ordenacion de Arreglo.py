# Matriz bidimensional de ejemplo
matriz = [[1, 5, 3], [4, 2, 6], [7, 8, 9]]

# Función para ordenar una fila de la matriz
def ordenar_fila(matriz, fila):
  """
  Función que ordena una fila específica de una matriz bidimensional en orden ascendente utilizando el algoritmo Bubble Sort.

  Parámetros:
    matriz: La matriz bidimensional en la que se ordena la fila.
    fila: El índice de la fila que se desea ordenar.

  Retorno:
    La matriz con la fila ordenada.
  """
  for i in range(len(matriz[fila])-1):
    for j in range(len(matriz[fila])-i-1):
      if matriz[fila][j] > matriz[fila][j+1]:
        matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
  return matriz



# Índice de la fila a ordenar
fila_a_ordenar = 0

# Ordenación de la fila
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Impresión de la matriz original
for fila in matriz:
  print(fila)

# Impresión de la matriz con la fila ordenada
print("Matriz con la fila ordenada:")
for fila in matriz_ordenada:
  print(fila)
