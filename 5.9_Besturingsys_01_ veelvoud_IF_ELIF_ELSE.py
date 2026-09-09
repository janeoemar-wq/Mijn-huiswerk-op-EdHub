# =============================# ==========================================
# # Opgave 1:
# # Gegeven is een int input getal_1 en getal_2 en drie print methodes. Schrijf een if statement dat controleert of getal1
# een veelvoud is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# # Zet de juiste print methode op de goede plek in je if statement.
# # Voorbeeld goede output: 10 is een veelvoud van 5
# # ==========================================
#
#
getal_1 = int(input("voer een getal in: "))
getal_2 = int(input("voer een getal in: "))

if getal_1 % getal_2 == 0:
    print(f"{getal_1} is een veelvoud van {getal_2}")
elif getal_2 > getal_1 == 0:
    print(f"{getal_2} is een veelvoud van {getal_1}")
else:
    print("geen van bedide getallen zijn een veelvoud")

