# Python
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = radians(int(input("Angulo : ")))

seno     = sin(angulo)
coseno   = cos(angulo)
tangente = tan(angulo)

print(
    f"\n Angulo Radiano ---> : {angulo:.2f}\n",
    f"\n Seno -------------> : {seno:.2f}",
    f"\n coseno -----------> : {coseno:.2f}",
    f"\n Tangente ---------> : {tangente:.2f}",
    "\n"
)
