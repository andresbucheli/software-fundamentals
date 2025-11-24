import random
random.seed()   #Prepare random number generator

print("Cuantas veces deseas lanzar el dado?")
numLa = int(input())
laRes = numLa
dado1 = 0
dado2 = 0
dado3 = 0
dado4 = 0
dado5 = 0
dado6 = 0
while laRes > 0:
    print("presione una letra para lanzar dato")
    a = input()
    dado = int(random.random() * 6) + 1
    if dado == 1:
        dado1 = dado1 + 1
    if dado == 2:
        dado2 = dado2 + 1
    if dado == 3:
        dado3 = dado3 + 1
    if dado == 4:
        dado4 = dado4 + 1
    if dado == 5:
        dado5 = dado5 + 1
    if dado == 6:
        dado6 = dado6 + 1
    print("dado: " + str(dado))
    laRes = laRes - 1
print("total de veces que salio el numero1: " + str(dado1))
print("total de veces que salio el numero2: " + str(dado2))
print("total de veces que salio el numero3: " + str(dado3))
print("total de veces que salio el numero4: " + str(dado4))
print("total de veces que salio el numero5: " + str(dado5))
print("total de veces que salio el numero6: " + str(dado6))
