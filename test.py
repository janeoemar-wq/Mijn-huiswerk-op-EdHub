# def print_jane_gek():
#     print("jane, hallo!!")
# print_jane_gek()
#
# def print_alibaba():
#     print("aliba 123456")
# print_alibaba()
#
# def print_ikbenboos():
#     print("ikbenboosopjouw")
# print_ikbenboos()
# factor = 5
# def print_tafel_van_vijf(getal,factor):
#     print(f"{getal} x {factor} = {getal*factor}")
# for i in range(1, 11):
#     print_tafel_van_vijf(i,i)

# factor = 3
# def print_tafelvandrie(getal, factor):
#     print(f"{getal} x {factor} = {getal*factor}")
# for i in range(1, 101):
#     print_tafelvandrie(i, factor)

# factor = 6
# def print_tafelvanzes(getal, factor):
#     print(f"{getal} x {factor} = {getal*factor}")
# for i in range(1, 10):
#     print_tafelvanzes(i, factor)

#  Maak met behulp van de bibliotheek (library) 'random' een functie die een willekeurig getal
# tussen 1 en 6 genereert.
# # Zorg dat de functie twee argumenten ontvangt, namelijk 'min' en 'max'. Voor het minimum (1)
# # en maximum (6).
# # Voer de functie 10 keer uit (met een for-loop). Als het willekeurige getal is gegenereert
# # print je het getal.


import random

def roll_dice(min, max):
    return random.randint(min, max)

def count_sixes(rolls):
    aantal_keer_zes = rolls.count(6)
    print(f"Er is {aantal_keer_zes} keer een 6 gegooid")

worpen = []

for i in range(10):
    worp = roll_dice(1, 6)
    worpen.append(worp)
    print(worp, end=" ")

print()
count_sixes(worpen)