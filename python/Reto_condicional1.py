import random
random.seed()   #Prepare random number generator

dado1 = int(random.random() * 6) + 1
dado2 = int(random.random() * 6) + 1
print("Presione una letra para lanzar dados ")
a = input()
if dado1 % 2 == 0:
    res = "Par"
    print("Dado1: " + str(dado1))
    print("El dado1 es: " + res)
else:
    res = "impar"
    print("El dado1 es: " + str(dado1))
    print("El dado1 es: " + res)
if dado2 % 2 == 0:
    res = "par"
    print("Dado2: " + str(dado2))
    print("El dado2 es: " + res)
else:
    res = "impar"
    print("El dado2 es: " + str(dado2))
    print("El dado1 es: " + res)
if dado1 == dado2:
    print("YOU WIN")
else:
    print("GAME OVER")
