# Python
# Escreva um programa que leia um valor em metros e o exiba convertido em : km , hm , dam , m , dm , cm e mm .

m = float(input("Metros: ").replace(",", "."))

km  = m / 1000
hm  = m / 100
dam = m / 10
dm  = m * 10
cm  = m * 100
mm  = m * 1000

print(
    f"\nQuilômetros  --> {km} km",
    f"\nHectômetros  --> {hm} hm",
    f"\nDecâmetros   --> {dam} dam",
    f"\nMetros       --> {m} m",
    f"\nDecímetros   --> {dm} dm",
    f"\nCentímetros  --> {cm} cm",
    f"\nMilímetros   --> {mm} mm",
    "\n"
)

