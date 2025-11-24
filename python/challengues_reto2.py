import random
random.seed()   #Prepare random number generator

print("Cuantas veces deseas lanzar el dado?")
numVe = int(input())
sumTo = 0
for i in range(1, numVe + 1, 1):
    resDa = int(random.random() * 6) + 1
    sumTo = sumTo + resDa
    print("lanzamiento " + str(i) + ": " + str(resDa))
print("Fin de los lanzamientos: La suma total final es: " + str(sumTo))
