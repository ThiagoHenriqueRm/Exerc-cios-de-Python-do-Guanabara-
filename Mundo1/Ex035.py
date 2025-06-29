# Python
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input("reta 1°: "))
r2 = int(input("reta 2°: "))
r3 = int(input("reta 3°: "))

calculo = r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2

if calculo : print("\n Essas retas formão um triangulo \n")
else       : print("\n Essas retas não fromão um triangulo \n")
