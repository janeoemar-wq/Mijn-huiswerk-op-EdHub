groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit",
          "De DaVinci Code", "Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"]

groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit",
          "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"]

groep1_set = set(groep1)
print("antwoord op: maak set groep 1: ")
print(groep1_set)
print()

print("antwoord op: maak set groep 2: ")
groep2_set = set(groep2)
print(groep2_set)
print()
# emeenschappelijke boeken: kies doorsnede van sets)
#De & betekent doorsnede: alleen de waarden die in beide sets voorkomen.
print("antwoord op Welke boeken zijn door beide groepen geleend?")
groep1_set & groep2_set
beide_groepen = groep1_set & groep2_set
print(beide_groepen)
print()

# Boeken geleend door slechts één groep:
# Welke boeken zijn alleen door Groep 1 geleend en niet door Groep 2? (Hint:
# Gebruik het verschil van sets)
verschil = groep1_set - groep2_set
print("het antwoord op boeken geleend door 1 groep")
print(verschil)
print()

#welke boeken zijn alleen door Groep 2 geleend en niet door Groep 1?
print("het antwoord op boeken geleend door groep2")
verschil = groep2_set - groep1_set
print(verschil)
print()

# . Aantal geleende keren per boek:
# o Maak een dictionary voor Groep 1 waarin de boeken de sleutels zijn en de
# waarden het aantal keren dat elk boek is geleend.
# o Maak een soortgelijke dictionary voor Groep 2.
print("maak key en value")
groep1_keys= ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit",
          "De DaVinci Code", "Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"]
boeken = {}
for boek in groep1:
    boeken[boek] = groep1.count(boek)
print()
print("boek               Aantal")
print("-------------------------")
for boek, aantal in boeken.items():
    print(f"{boek:<20}{aantal}")
print()
print()
# tabel maken voor groep 2

boeken = {}

for boek in groep1:
    boeken[boek] = groep1.count(boek)
print("++++++++++++++++++++++++++++++++++++++")
print("| boek                       Aantal | ")
print("++++++++++++++++++++++++++++++++++++++")
for boek, aantal in boeken.items():
    print(f"| {boek:<20} | {aantal} | ")
# tabel maken voor groep 2
groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit",
          "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"]
boeken = {}
for boek in groep2:
    boeken[boek] = groep2.count(boek)
    print()
print("++++++++++++++++++++++++++++++++++++++")
print("| boek                        Aantal  ")
print("++++++++++++++++++++++++++++++++++++++")
for boek, aantal in boeken.items():
    print(f"| {boek:<20} | {aantal} | ")
# Tabellen naast elkaar
print()
print("     GROEP 1                                 GROEP 2")
print("++++++++++++++++++++++++++       +++++++++++++++++++++++++++++++++++++++")
print("| boek              Aantal      | boek                      Aantal")
print("++++++++++++++++++++++++++       +++++++++++++++++++++++++++++++++++++++")

boeken_groep1 = {}
boeken_groep2 = {}
for boek in groep1:
    boeken_groep1[boek] = groep1.count(boek)
for boek in groep2:
    boeken_groep2[boek] = groep2.count(boek)
lijst1 = list(boeken_groep1.items())
lijst2 = list(boeken_groep2.items())
for i in range(max(len(lijst1), len(lijst2))):
    if i < len(lijst1):
        boek1, aantal1 = lijst1[i]
        links = f"| {'':<20} | {'':^6} |"
    else:
        links = "                          |        |               |"
    if i < len(lijst2):
        boek2, aantal2 = lijst2[i]
        rechts = f"| {boek2:<20} | {aantal2:^6} |"
    else:
        links = "| | |"
    print(links, " ", rechts)
print("+----------------------+--------+ +----------------------+--------+")


# meest geleende boek:
# o Gebruik de dictionary van vraag 4 om te bepalen welk boek het meest is
# geleend door Groep 1 en welk boek door Groep 2.

# meest_groep1 = max(boeken_groep1, key=boeken_groep1.get)
# meest_groep2 = max(boeken_groep2, key=boeken_groep2.get)
# print("Meest geleende boek Groep 1:")
# print(meest_groep1, boeken_groep1[meest_groep1])
# print()
# print("Meest geleende boek Groep 2:")
# print(meest_groep2, boeken_groep2[meest_groep2])