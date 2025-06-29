# Python
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

n = randint(0, 5)
entrada = int(input("Tente adivinhar o numero (0 a 5): "))

if entrada == n:
    print(f"\n -> {n} esta correto!!\n")
else: 
    print(f"\n -> {entrada} esta incorreto, o numero éra : {n}\n")
