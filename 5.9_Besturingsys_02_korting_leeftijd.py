# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================
korting = 100
korting  = 50
korting  = 0
prijs = 6.00
leeftijd = int(input("wat is uw leeftijd: "))

if leeftijd < 5:
    print(f"Op basis van uw leeftijd van {leeftijd} is de toegang gratis")
elif leeftijd < 12:
    print(f"op basis van uw leeftijd van {leeftijd} jaar krijgt u de de toegangkaartje voor de halve prijs")
elif leeftijd < 54:
    print(f"Op basis van uw leeftijd van {leeftijd} jaar krijgt u geen korting op uw kaartje")
else:
    print("Op basis van uw leeftijd van {leeftijd} is de toegang gratis")