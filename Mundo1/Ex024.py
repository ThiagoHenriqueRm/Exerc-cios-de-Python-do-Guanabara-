# Python
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Cidade : ")).strip()
ver = cidade[:5].upper() == "SANTO"

print(f'\n Começa com "Santo"? -> {ver}\n')
