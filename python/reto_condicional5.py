print("Introduzca el tipo de documento (CC, PS, CE, CI)")
tiDo = input()
print("Introduzca el numero de identificación")
num = input()
print("Ingrese los nombres")
nom = input()
print("Ingrese los apellidos")
ape = input()
print("Ingrese genero")
gen = input()
print("Ingrese año de nacimiento")
añoNa = int(input())
print("Ingrese dirrecion")
dir = input()
print("Ingrese numero de telefono")
tel = input()
print("Ingrese valor del salario")
sala = float(input())
if sala >= 2000000:
    if gen == "femenino":
        inc = sala * 3 / 100
        nueSala = sala + inc
        print("El salario final de  " + nom + "  " + ape + "  es " + str(nueSala))
    else:
        inc = sala * 2.5 / 100
        nueSala = sala + inc
        print("El salario final de  " + nom + "  " + ape + "  es " + str(nueSala))
else:
    if sala > 1200000 or sala > 2000000:
        inc = sala * 5 / 100
        nueSala = sala + inc
        print("El salario final de  " + nom + "  " + ape + "  es " + str(nueSala))
    else:
        if gen == "femenino":
            inc = sala * 10 / 100
            nueSala = sala + inc
            print("El salario final de  " + nom + "  " + ape + "  es " + str(nueSala))
        else:
            inc = sala * 8 / 100
            nueSala = sala + inc
            print("El salario final de  " + nom + "  " + ape + "  es " + str(nueSala))
