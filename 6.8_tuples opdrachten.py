#https://(github.com/hogeschoolnovi/programming-fundamentals-tuples-loops/blob/
#uitwerkingen/Tuples.py)

steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
for stad in steden:
    print(stad)


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple
nieuwe_tuple  = tuple1 + tuple2
print(nieuwe_tuple)

# Definieer een tuple met verschillende soorten gegevens
# (bijvoorbeeld getallen, strings, booleans, etc.
gegevens = ("Jane", 8.5, "Frank", 2026, "Joke", 9.5, "Fanny", 2020, 1999, 2.5)
print(gegevens)

# Print enkele elementen van de tuple namelijk het eerste,
# een subset (vanaf index 2 tot index 5) en het laatste element
print(gegevens[0])
print(gegevens[2:5])
print(gegevens[-1])

## Maak een tuple met een naam en een leeftijd
persoon = "jane", 55
print(persoon)

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen
# (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)
#tuple unpacking.
persoon = "jane", 55
naam, leeftijd = persoon
print(naam)
print(leeftijd)
print()

persoon = "jane", 55
naam, leeftijd = persoon
print(leeftijd)
print(naam)

