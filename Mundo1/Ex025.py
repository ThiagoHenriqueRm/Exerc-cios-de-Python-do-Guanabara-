# Python
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Seu nome todo : ")).strip()
ver = ("SILVA" in nome.upper())

print(f"\n Tem Silva no nome ? : {ver}\n")
