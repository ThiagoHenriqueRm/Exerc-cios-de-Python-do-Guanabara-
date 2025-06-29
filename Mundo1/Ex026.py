# Python
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# E em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Sua frasa : ")).upper().strip()

contA     = frase.count("A")
primairoA = frase.find("A")
ultimoA   = frase.rfind("A")

print(
    f"\n lateas A -------------------> : {contA}",
    f"\n 1° A está na posição -------> : {primairoA+1}",
    f"\n Ultimo A está na posição ---> : {ultimoA}",
    "\n"
)
