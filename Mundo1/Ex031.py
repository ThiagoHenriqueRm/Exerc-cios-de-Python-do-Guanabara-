# Python
# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Distancia em km : "))

if   distancia <= 200 : preco = (distancia * 0.50) 
else                  : preco = (distancia * 0.45)

print(f"\n O preço de uma viagme de {distancia}Km é R${preco:.2f} \n")
