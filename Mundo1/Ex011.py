# Python
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Largura : ").replace(",", "."))
altura  = float(input("Altura  : ").replace(",", "."))

area  = ( largura * altura )
tinta = ( area / 2 )

print(
    f"\n Area -------------> : {area}m²",
    f"\n Tinta necessaria -> : {tinta}L",
    "\n"
)
