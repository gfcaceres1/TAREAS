import random

# Ciudades
ciudades = ["Quito", "Bogotá", "Buenos Aires", "Madrid"]

# Días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Semanas
semanas = [1, 2, 3, 4]

# Crear matriz 3D
temperaturas = [[[0 for i in range(len(dias_semana))] for j in range(len(semanas))] for k in range(len(ciudades))]

# Llenar la matriz con datos de prueba (reemplazar con datos reales)
for ciudad in range(len(ciudades)):
  for semana in range(len(semanas)):
    for dia in range(len(dias_semana)):
      temperaturas[ciudad][semana][dia] = round(random.uniform(10, 30), 1)

# Calcular promedios por ciudad y semana
promedios = {}
for ciudad in ciudades:
  promedios[ciudad] = {}
  for semana in semanas:
    promedios[ciudad][semana] = 0
    for dia in dias_semana:
      promedios[ciudad][semana] += temperaturas[ciudades.index(ciudad)][semanas.index(semana)][dias_semana.index(dia)]
    promedios[ciudad][semana] /= len(dias_semana)

# Mostrar promedios
for ciudad, semanas_promedios in promedios.items():
  print(f"Ciudad: {ciudad}")
  for semana, promedio in semanas_promedios.items():
    print(f"Semana {semana}: {promedio:.1f}°C")

