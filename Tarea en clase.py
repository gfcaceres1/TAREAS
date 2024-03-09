def conversor(grados_cent):
    Fahrenheit = (9 / 5) * (grados_cent) + 32    #transformando grados centigrado a grados Fahrenheit
    Kelvin = 273.15 + grados_cent    #transformacion de grados centigrados a grados kelvin

    return Fahrenheit, Kelvin

centigrados=int(input("Ingrese los grados centigrados="))

result_far, result_kelvin =conversor(centigrados)

print(centigrados, "grados centigrados es igual a ", result_far, "grados Fahreneit")
print("Kelvin es igual a", result_kelvin)