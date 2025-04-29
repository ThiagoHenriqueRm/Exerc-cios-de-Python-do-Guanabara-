# Python
# Crie um algoritmo que leia um número e mostre o seu Dobro, Triplo e a Raiz Quadrada

n = int(input("Numero : "))

dobro  = n * 2
triplo = n * 3
raiz   = n ** (1/2)

print(
    f"\n Dobro ---------> : {dobro}",
    f"\n Triplo --------> : {triplo}",
    f"\n Raiz Quadrada -> : {raiz:.2f}"
    "\n"
)
