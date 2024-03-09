def calcular_promedio_temperatura(ciudades, semanas, temperaturas):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.

    Parámetros:
      ciudades: Lista de nombres de ciudades.
      semanas: Lista de números de semana.
      temperaturas: Diccionario con las temperaturas de cada ciudad y semana.

    Retorno:
      Diccionario con las temperaturas promedio de cada ciudad.
    """
    promedios = {}
    for ciudad in ciudades:
        promedios[ciudad] = []
        for semana in semanas:
            # Obtener las temperaturas de la ciudad y semana actual
            temps = temperaturas[ciudad][semana]

            # Si no hay datos para la ciudad y semana actual, continuar
            if not temps:
                continue

            # Calcular el promedio de las temperaturas
            promedio = sum(temps) / len(temps)
            promedios[ciudad].append(promedio)
    return promedios


# Obtener datos del usuario
ciudades = []
while True:
    ciudad = input("Ingrese el nombre de una ciudad (o 'salir' para terminar): ")
    if ciudad.lower() == "salir":
        break
    ciudades.append(ciudad)

semanas = []
while True:
    try:
        numero_semana = int(input("Ingrese el número de una semana (1-52): "))
        if 1 <= numero_semana <= 52:
            semanas.append(numero_semana)
            break
        else:
            print("Número de semana inválido. Debe ser un número entre 1 y 52.")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

temperaturas = {}
for ciudad in ciudades:
    temperaturas[ciudad] = {}
    for semana in semanas:
        temperaturas[ciudad][semana] = []
        while True:
            try:
                temperatura = float(input(f"Ingrese una temperatura para {ciudad} en la semana {semana}: "))
                temperaturas[ciudad][semana].append(temperatura)
                break
            except ValueError:
                print("Entrada inválida. Debe ser un número decimal.")

# Calcular y mostrar los promedios
promedios_ciudades = calcular_promedio_temperatura(ciudades, semanas, temperaturas)

for ciudad, promedios in promedios_ciudades.items():
    print(f"Ciudad: {ciudad}")
    for semana, promedio in enumerate(promedios):
        print(f"Semana {semana + 1}: {promedio:.2f}°C")
    print()
