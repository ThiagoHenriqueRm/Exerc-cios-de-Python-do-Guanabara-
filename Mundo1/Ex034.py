# Python 
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Salario : R$").replace(",", "."))

if salario > 1250.00: 
    aumento = ((10/100) * salario)
    print(f"\n R${salario:.2f} (+10%) -> R${salario + aumento:.2f} \n")

else: 
    aumento = ((15/100) * salario)
    print(f"\n R${salario:.2f} (+15%) -> R${salario + aumento:.2f} \n")