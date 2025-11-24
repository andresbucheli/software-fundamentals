numero = 0
print("Introduzca el valor del número: ")
numero = int(input())
if abs(numero) % 2 == 0:
    res = "Par"
    print("El Numero es: " + res)
else:
    res = "Impar"
    print("El Numero es: " + res)
