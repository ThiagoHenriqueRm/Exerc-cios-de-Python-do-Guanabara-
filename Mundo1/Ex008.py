# Python
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Metros : ").replace(",", "."))

km  = m / 1000
hm  = m / 100
dam = m / 10
dm  = m * 10
cm  = m * 100
mm  = m * 1000

print(
    f"\n Kilometros --> : {km}km   ",
    f"\n Hequitros ---> : {hm}hm   ",
    f"\n Decametros --> : {dam}dam ",
    f"\n Metos -------> : {m}m     ",
    f"\n Decimetros --> : {dm}dm   ",
    f"\n Centimetros -> : {cm}cm   ",
    f"\n Milimetros --> : {mm}mm   ",
    "\n"
)
