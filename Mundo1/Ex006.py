# Python
from os import system
system("clear")

n = int(input("Numero : "))

dobro  = n * 2
triplo = n * 3
rais   = n ** (1/2)

print(
    f"\n Dobro ---------> : {dobro}",
    f"\n Triplo --------> : {triplo}",
    f"\n Raiz Quadrada -> : {rais:.2f}"
    "\n"
)
