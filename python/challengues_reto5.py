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
    if dado1 == dado2:
        lanPar = lanPar + 1
    if dado1 != dado2:
        lanImpar = lanImpar + 1
    contador = contador + 1
print("lanzamientos finalizados")
print("total de lanzamientos pares: " + str(lanPar))
print("total de lanzamientos impares: " + str(lanImpar))
