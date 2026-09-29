print("*********************************          **********************************")
print("  *************************                      *************************")
print("     ******************          Deurenspel           *****************")


print()
print("Je staat in een straat.")
print("Je ziet drie deuren:")
print("1. Een rode deur")
print("2. Een gele deur")
print("3. Een blauwe deur")

keuze = input("Welke deur kies je? (1, 2 of 3): ")

# Rode deur
if keuze == "1":
    print()
    print("Je hebt de rode deur gekozen, je komt in de rode kamer.")
    print()
    print("Er staat een groene deur.")

    deur = input("Ga je door de groene deur? (ja/nee): ")

    if deur == "ja":
        print()
        print("Gefeliciteerd!")
        print("Je bent veilig ontsnapt.")
        print("FINISH!")
    else:
        print()
        print("Je blijft in de rode kamer.")
        print("Het monster vindt je...")
        print("DOOD DOOR MONSTER!")

# Gele deur
elif keuze == "2":
    print()
    print("Je hebt de gele deur gekozen.")
    print("Je komt in de gele kamer.")
    print("Er staat een groene deur.")

    deur = input("Ga je door de groene deur? (ja/nee): ")

    if deur == "ja":
        print()
        print("O nee!")
        print("Achter de deur zit een monster.")
        print("DOOD DOOR MONSTER!")
    else:
        print()
        print("Je blijft in de gele kamer.")
        print("Het monster komt dichterbij...")
        print("DOOD DOOR MONSTER!")

# Blauwe deur
elif keuze == "3":
    print()
    print("Je hebt de blauwe deur gekozen.")
    print("Je komt in de blauwe kamer.")
    print("Er zijn twee deuren:")
    print("1. Een rode deur")
    print("2. Een groene deur")

    deur = input("Welke deur kies je? (1 of 2): ")

    if deur == "1":
        print()
        print("Je gaat door de rode deur.")
        print("Je komt in de rode kamer.")
        print("Er is een groene deur.")

        deur2 = input("Ga je door de groene deur? (ja/nee): ")

        if deur2 == "ja":
            print()
            print("Gefeliciteerd!")
            print("Je hebt het spel gewonnen!")
            print("FINISH!")
        else:
            print()
            print("Het monster heeft je gevonden.")
            print("DOOD DOOR MONSTER!")

    elif deur == "2":
        print()
        print("Je opent de groene deur...")
        print("O nee! Een monster!")
        print("DOOD DOOR MONSTER!")

    else:
        print()
        print("Ongeldige keuze.")

# Ongeldige startkeuze
else:
    print()
    print("Ongeldige keuze.")
    print("Kies alleen 1, 2 of 3.")

print()
print("Einde van het spel.")