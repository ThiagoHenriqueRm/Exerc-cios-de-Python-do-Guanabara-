# Python
# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = str(input("Nome do 1° aluno : "))
n2 = str(input("Nome do 2° aluno : "))
n3 = str(input("Nome do 3° aluno : "))
n4 = str(input("Nome do 4° aluno : "))

alunos = [n1, n2, n3, n4]
shuffle(alunos)

print(f"\n A ordem é : {alunos}\n")
