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


# Ejemplo de uso
ciudades = ["Quito", "Guayaquil", "Cuenca"]
semanas = [1, 2, 3, 4]
temperaturas = {
    "Quito": {
        1: [20, 22, 21, 19],
        2: [21, 23, 22, 20],
        3: [22, 24, 23, 21],
        4: [23, 25, 24, 22],
    },
    "Guayaquil": {
        1: [28, 29, 27, 26],
        2: [29, 30, 28, 27],
        3: [30, 31, 29, 28],
        4: [31, 32, 30, 29],
    },
    "Cuenca": {
        1: [18, 20, 19, 17],
        2: [19, 21, 20, 18],
        3: [20, 22, 21, 19],
        4: [21, 23, 22, 20],
    },
}

promedios_ciudades = calcular_promedio_temperatura(ciudades, semanas, temperaturas)

# Imprimir los resultados
for ciudad, promedios in promedios_ciudades.items():
    print(f"Ciudad: {ciudad}")
    for semana, promedio in enumerate(promedios):
        print(f"Semana {semana + 1}: {promedio:.2f}°C")
    print()
