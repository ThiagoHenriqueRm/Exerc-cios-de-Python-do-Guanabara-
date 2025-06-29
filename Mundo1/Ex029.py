# Python
# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

vlocidade = float(input("Velocidade do carro : "))

if vlocidade > 80:
    multa = 7 * (vlocidade - 80)
    print(
        f"\n {vlocidade}km/h ultrapassa 80km/h.",
        f"\n multado em R${multa:.2f}!",
        "\n"
    )
else:
    print(f"\n {vlocidade}km/h Tudo OK... \n")
