from operator import contains

# list_of_nummers = [1, 2, 3, 4, 5, 6]
# for x in list_of_nummers:
#      print(x)
# for x in list_of_nummers:
#     print(f"{x}")
# #print(list_of_nummers[::-4])
#
# some_list = 1, 2, 3, 4, 5, 6
# for x in some_list:
#     if x <=5:
#         print(x)
#
# boodschappenlijst = ["brood", "kaas", "eieren", "melk", "beleg"]
# print(boodschappenlijst[0])
# print(boodschappenlijst[2])
# print(boodschappenlijst[1:4])
#
# lijst = 1, 2, 3, 4, 5, 6
# print(lijst)
# print(lijst[0])
#=============================================================
#  Maak een lijst van tuples, waarbij elke tuple bestaat uit een student en zijn/haar cijfer.
# Bijvoorbeeld:
# studenten = [("Anneke", 8.5), ("Bart", 7.0), ("Charlie", 6.2),
# ("Daphne", 9.1)]
# 2. Maak een functie waarin je met een for-loop:
#  - Alle namen van de studenten met hun bijbehorende cijfer af afdrukt in een nette
# opsomming.
#  - De gemiddelde score van alle studenten berekent.
# 3. Toon de volgende resultaten aan het einde van het programma:
#  - De gemiddelde score van alle studenten.
#  - De naam en het cijfer van de student met het hoogste cijfer.
# Voorbeeld uitvoer van het programma:
# Studenten en hun cijfers:
# Anneke - 8.5
# Bart - 7.0
# Charlie - 6.2
# Daphne - 9.1
print(        "Overzicht resultaat studenten")
print()
studenten = [("Anneke", 8.5),
             ("Bram", 3.5),
             ("Marieke", 7.5),
             ("Bart", 1.5),
             ("Frank", 8.0),
             ("Els", 5.5)]
totaal = 0
for naam, cijfer in studenten:
#naam = toon de naam < = lijn de naam links uit, 10 = reserveer 10 plaatsen daarna wordt het cijfer afgedrukt
    totaal = totaal + cijfer
hoogste_cijfer = 0
beste_student = ""

#Toon de volgende resultaten aan het einde van het programma:
# - De gemiddelde score van alle studenten.
# - De naam en het cijfer van de student met het hoogste cijfe

for naam, cijfer in studenten:
    print(f"{naam:<10}{cijfer}")

    if cijfer > hoogste_cijfer:
        hoogste_cijfer = cijfer
        beste_student = naam
gemiddelde = totaal / len(studenten)
print()
print("Gemiddelde score:", gemiddelde)
print("Hoogste cijfer:", beste_student, "-", hoogste_cijfer)
print()

def student_toevoegen(studentenlijst) :
    naam = input("Voeg nieuw student toe:")
    cijfer = float(input("Voeg nieuw cijfer toe:"))

    studentenlijst.append((naam, cijfer))
student_toevoegen(studenten)
print()
print("nieuwe studentenlijst:")

for naam, cijfer in studenten:
    print(f"{naam:<10}{cijfer}")

def student_zoeken(studentenlijst) :
    while True:
        zoeknaam = input("Welk student wil je zoeken:")
        for naam, cijfer in studentenlijst:
            if naam.lower() == zoeknaam.lower():
                print("student:", naam)
                print("cijfer:", cijfer)
                return
        print("student niet gevonden. Probeer opnieuw")
student_zoeken(studenten)
# sorteren met LAMBDA
# def studenten_sorteren(studentenlijst) :
#     studentenlijst.sort(key=lambda student: student[1], reverse=True)
#     print()
#     print("Di zijn de studenten gesorteerd op cijfer:")
#     for naam, cijfer in studentenlijst:
#         print(f"{naam:<10}{cijfer}")
# studenten_sorteren(studenten)

#sorteren als functie
def pak_cijfer(studenten):
    return studenten[1]
def studenten_sorteren_cijfer(studentenlijst):
    studentenlijst.sort(key=pak_cijfer, reverse=True)
    print()
    print("Overzicht studenten gesorteerd op cijfer")

    for naam, cijfer in studentenlijst:
        print(f"{naam:<10}{cijfer}")
studenten_sorteren_cijfer(studenten)

def pak_naam(studenten):
    return studenten[0]
def studenten_sorteren_naam(studentenlijst):
    studentenlijst.sort(key=pak_naam)
    print()
    print("Overzicht studenten gesorteerd op naam")

    for naam, cijfer in studentenlijst:
        print(f"{naam:<10}{cijfer}")
studenten_sorteren_naam(studenten)

#sorteren op alfabet zonder key PAK
def studenten_sorteren_naam(studentenlijst):
    studentenlijst.sort()
    print()
    print("Overzicht studenten op alfabetische volgorde")
    for naam, cijfer in studentenlijst:
        print(f"{naam:<10}{cijfer}")
studenten_sorteren_naam(studenten)