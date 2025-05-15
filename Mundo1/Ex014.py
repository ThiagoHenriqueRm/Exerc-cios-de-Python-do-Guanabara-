# Python
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


c = float(input("Temperatura °C:").replace(",", "."))
f = 9 * c / 5 + 32 

print(f"\n {c:.1f}°C -> {f:.1f}°F\n")
