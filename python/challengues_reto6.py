import random
random.seed()   #Prepare random number generator

toLan = 0
sumDa = 0
numPar = 0
numImpar = 0
lanDa = "S"
while lanDa == "S" or lanDa == "s":
    print("Oprima una letra para lanzar los dados")
    a = input()
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    toLan = toLan + 1
    sumDa = sumDa + dado1 + dado2
    print("Lanzamiento #" + str(toLan) + ":    Dado 1: " + str(dado1) + "          Dado2: " + str(dado2))
    if dado1 == dado2:
        numPar = numPar + 1
    if dado1 != dado2:
        numImpar = numImpar + 1
    print("Desea volver a lanzar los dados")
    print("Oprima 'S'(si)")
    lanDa = input()
print("reporte final de resultados")
print("Total de tiros efectuados: " + str(toLan))
print("suma total de los tiros efectuados: " + str(sumDa))
print("total de pares generados: " + str(numPar))
print("total de impares generados: " + str(numImpar))
