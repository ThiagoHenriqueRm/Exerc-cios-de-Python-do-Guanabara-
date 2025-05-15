# Python
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

n1 = str(input("Nome do 1° aluno : "))
n2 = str(input("Nome do 2° aluno : "))
n3 = str(input("Nome do 3° aluno : "))
n4 = str(input("Nome do 4° aluno : "))

alunos = [n1, n2, n3, n4]
escolha = choice(alunos)

print(f'\n O escolhido foi "{escolha}"\n')

