# Python
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

co = float(input("cateto Oposto : ").replace(",", "."))
ca = float(input("cateto Adjacente : ").replace(",", "."))

hi = ( ((co**2 + ca**2))**(1/2) )

print(
    f"\n Cateto Oposto ----> : {co}",
    f"\n Cateto Adjacente -> : {ca}",
    f"\n Hipotenusa -------> : {hi:.2f}",
    "\n"
)
