# Python
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias  = int(input("Dias : "))
km    = float(input("Km rodados : ").replace(",", "."))
preco = (60 * dias) + (0.15 * km)

print(f"\n R${preco:.2f} a pagar \n")
