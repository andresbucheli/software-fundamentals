import random
random.seed()   #Prepare random number generator

dado = int(random.random() * 6) + 1
print("Presione una letra para lanzar el dado ")
a = input()
if dado % 2 == 0:
    res = "Par"
    print("Dado: " + str(dado))
    print("El dado es: " + res)
else:
    res = "impar"
    print("El dado es: " + str(dado))
    print("El dado es: " + res)
