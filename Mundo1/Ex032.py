# Python
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input("Ano (0 para ano atual) : "))
if ano == 0: ano = date.today().year

bi = (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)

if bi: print(f"\n O ano {ano} é bissexto \n")
else : print(f"\n O ano {ano} não é Bissexto \n")