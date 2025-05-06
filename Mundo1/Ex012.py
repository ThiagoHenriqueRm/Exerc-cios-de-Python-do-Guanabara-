# Python
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input("Preço : R$").replace(",", "."))
desconto = ( produto - ((produto/100) * 5) )

print(f"\n R${produto:.2f} (-5%) -> R${desconto:.2f}\n")
