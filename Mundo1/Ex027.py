# Python
# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Nome completa : ")).split()

nome1 = nome[0]
nomeF = nome[len(nome) - 1]

print(
    f"\n 1° Nome -----> : {nome1}",
    f"\n Ultimo Nome -> : {nomeF}",
    "\n"
)