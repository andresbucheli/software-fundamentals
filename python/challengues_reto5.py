import random
random.seed()   #Prepare random number generator

lanImpar = 0
lanPar = 0
numLa = 0
contador = 1
print("ingrese el numero de lanzamientos")
numLa = int(input())
while contador <= numLa:
    print("presione una letra para lanzar los dados")
    a = input()
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    print(" dado1:" + str(dado1))
    print("dado2:" + str(dado2))
    resDados = dado1 + dado2
    if resDados % 2 == 0:
        lanPar = lanPar + 1
    else:
        lanImpar = lanImpar + 1
    contador = contador + 1
print("lanzamientos finalizados")
print("total de lanzamientos pares: " + str(lanPar))
print("total de lanzamientos impares: " + str(lanImpar))
