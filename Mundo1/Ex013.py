# Python
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Salario : R$").replace(",", "."))
aumento = ( salario + ((salario/100) * 15 ))

print(f"\n R${salario:.2f} (+15%) -> R${aumento:.2f}\n")
