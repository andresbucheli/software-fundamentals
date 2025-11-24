print("Introduzca el numero")
numero = float(input())
if numero > 0:
    if numero % 2 == 0:
        print("El numero " + str(numero) + " es par positivo")
    else:
        print("El numero " + str(numero) + " es impar positivo")
else:
    if -numero % 2 == 0:
        print("El numero " + str(numero) + " es par negativo")
    else:
        print("El numero " + str(numero) + " es impar negativo")
