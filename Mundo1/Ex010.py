# Python
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Quanto dinheiro você tem? R$").replace(",", "."))
dolares = reais / 5

print(f"\n R${reais} -> US${dolares:.2f}\n")
