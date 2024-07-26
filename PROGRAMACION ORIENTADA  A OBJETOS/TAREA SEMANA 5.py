def calcular_imc(peso: float, altura: float) -> float:
  """
  Calcula el Índice de Masa Corporal (IMC) de una persona.

  Parámetros:
    peso: Peso de la persona en kilogramos (float).
    altura: Altura de la persona en metros (float).

  Retorno:
    Valor del IMC (float).
  """
  if altura <= 0:
    raise ValueError("La altura no puede ser menor o igual a 0.")
  imc = peso / (altura * altura)
  return imc

def clasificar_imc(imc: float) -> str:
  """
  Clasifica el IMC en una categoría de peso según la Organización Mundial de la Salud (OMS).

  Parámetros:
    imc: Valor del IMC (float).

  Retorno:
    Clasificación del IMC (string):
      - "Bajo peso"
      - "Peso normal"
      - "Sobrepeso"
      - "Obesidad grado I"
      - "Obesidad grado II"
      - "Obesidad grado III"
  """
  if imc < 18.5:
    return "Bajo peso"
  elif imc < 25:
    return "Peso normal"
  elif imc < 30:
    return "Sobrepeso"
  elif imc < 35:
    return "Obesidad grado I"
  elif imc < 40:
    return "Obesidad grado II"
  else:
    return "Obesidad grado III"

# Ejemplo de uso
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))


imc = calcular_imc(peso, altura)
clasificacion = clasificar_imc(imc)

print(f"Su IMC es: {imc:.2f}")
print(f"Su clasificación de peso es: {clasificacion}")
