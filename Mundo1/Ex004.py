# Python
# Feça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as finformações possieis sobra ela.

entrada = input("\nEntrda : ")

tipo        = type(entrada)
ascii       = entrada.isascii()
alfabetico  = entrada.isalpha()
minuscula   = entrada.islower()
maiuscula   = entrada.isupper()
captalizada = entrada.istitle()
alfanumerio = entrada.isalnum()
numerico    = entrada.isnumeric()

print(
    f"\n INFORMAÇOES -> {entrada} \n",
    
    f"\n Tipo? ---------> : {tipo}",
    f"\n Ascii? --------> : {ascii}",
    f"\n Alfabetico? ---> : {alfabetico}",
    f"\n Minuscula? ----> : {minuscula}",
    f"\n Maiuscula? ----> : {maiuscula}",
    f"\n Captalizada? --> : {captalizada}",
    f"\n Alfanumerico? -> : {alfanumerio}",
    f"\n Numerico? -----> : {numerico}",
    "\n"
)
