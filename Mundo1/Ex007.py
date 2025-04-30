# Python
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1    = float(input("Nota 1 : ").replace(",", "."))
n2    = float(input("Nota 2 : ").replace(",", "."))
media = (n1 + n2) / 2

print(
    f"\n nota 1 -> : {n1}",
    f"\n nota 2 -> : {n2}",
    f"\n Media --> : {media:.1f}",
    "\n"
)
