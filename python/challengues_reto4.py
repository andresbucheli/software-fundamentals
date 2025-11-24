import random
random.seed()   #Prepare random number generator

numLa = 0
parde6 = False
while parde6 == False:
    print("presione una letra para lanzar los dados")
    a = input()
    numLa = numLa + 1
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    print("lanzamiento #" + str(numLa))
    print(" dado1:" + str(dado1))
    print("dado2:" + str(dado2))
    if dado1 == 6 and dado2 == 6:
        print("FIN se ha obtenido un par de 6")
        parde6 = True
