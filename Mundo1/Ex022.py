# Python
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input("Nome : ")).strip()

maiusculas = nome.upper()
minusculas = nome.lower()
letras     = len("".join(nome.split()))
letras1    = len(nome.split()[0])

print(
    f"\n INFORMAÇOS -> {nome}:",
    "\n",
    f"\n Maiusculas -----------------> : {maiusculas}",
    f"\n Minusculas -----------------> : {minusculas}",
    f"\n Numero de letras -----------> : {letras}",
    f"\n Numero de letras de nome 1 -> : {letras1}",
    "\n"
)
