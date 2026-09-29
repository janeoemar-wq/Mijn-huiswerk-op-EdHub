# ==========================================
#veel gebruikte codes voor dictionary
# cijfers.keys() # alleen de namen
# cijfers.values() # alleen de cijfers
# cijfers.items() # namen én cijfers
# =======================================
# bij een dictionary-vergelijking maakt de volgorde niet uit,
# maar de combinatie van key en value wel.
# Voorbeeld Opdracht
#
# Maak een dictionary genaamd 'fruit' met daarin de sleutels 'appel' en 'banaan'.
# Geef 'appel' de value 'rood' en 'banaan' de value 'geel'.
# Print vervolgens de kleur van de banaan door de naam 'banaan' te gebruiken.
#
# Verwachte uitkomst:  geel
# ==========================================

# dictionary met kleuren als values
fruit = {'appel': 'rood', 'banaan': 'geel'}

# print de kleur van de banaan
print(fruit['banaan'])  # Het resultaat is: geel

drank = {'melk': 'wit', 'water': 'doorzichtig', 'çola': 'zwart'}
print(drank['melk'])

ontbijt = {'brood': 'wit', 'koffie': 'zwart'}
print(ontbijt['koffie'])

# ==========================================
# Opdracht 1:
# Gegeven is de dictionary 'boodschappen' met daarin de keys 'Appels' en 'Brood'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste
# resultaat krijgt.
#
# Opdracht 1a:
# Roep de waarde aan die hoort bij de naam 'Brood'
# Verwachte uitkomst: 2
#
# Opdracht 1b:
# Gebruik de get() methode op de waarde 'Appels' en 'Bananen'. Zorg dat als de naam niet bestaat, de tekst 'Niet gevonden' wordt geprint.
# ==========================================

boodschappen = {'Appels': 6, 'Brood': 2}
boodschappen = {'brood':3, 'fruit': 2}
print(boodschappen['fruit'])


# ==========================================
# Opdracht 2:
# Gegeven zijn vier boodschappenlijstjes als dictionary. Je kan een if statement gebruiken en
# de == operator om te vergelijken.
#
# Opdracht 2a:
# Vergelijk de boodschappenlijstjes van Marie en Raj. Als de lijstjes gelijk zijn, print
# 'De boodschappenlijstjes zijn gelijk.'.

lijst_marie = {'brood': 101, 'drank': 1}
lijst_raj = {'brood': 10, 'drank': 1}
if lijst_marie == lijst_raj:
    print("De lijsten zijn gelijk")
else:
    print("de lijsten zijn niet gelijk")

# Opdracht 2b:
# Vergelijk de boodschappenlijstjes (Marie, Raj en Jan). Als de lijstjes gelijk zijn, print
# 'De boodschappenlijstjes zijn gelijk.'.
# Waarom worden deze lijstjes wel/niet als gelijk beschouwd?
#
# Opdracht 2c:
# Vergelijk nu op dezelfde manier alle lijstjes. Zijn ze gelijk? Waarom wel/niet?
# ==========================================

boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}
boodschappenlijst_jan = {'Appels': 6, 'Brood': 1}
boodschappenlijst_karel = {'Appels': 6, 'Brood': 25}
# sleutel = brood/ appel
#waarde  = aantal


# ==========================================
# Opdracht 2:
# De voorraad van meubelwinkel 'Op Eigen Houtje' is als volgt:
# Gegeven is de dictionary 'meubels' met daarin de keys 'banken' en 'stoelen'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat
# krijgt.

meubels = {'banken':10, 'stoelen':20}
meubels['banken'] -= 6
print(meubels)

#
# Opdracht 2a:
# Er worden 6 banken verkocht. Pas de waarde van de naam 'banken' aan en print de
# aangepaste dictionary
# Verwachte uitkomst: {'banken': 4, 'stoelen': 20}

meubels = {'banken': 10, 'stoelen': 20}
# Opdracht 2a:
meubels['banken'] -= 6
print(meubels)  # Het resultaat is: {'banken': 4, 'stoelen': 20}

# Opdracht 2b:
# Er komen klachten dat klanten door eerder gekochte stoelen zijn gezakt. De winkel besluit om de stoelen uit het assortiment te halen.
# Verwijder de naam 'stoelen' (en daarmee ook de bijbehorende value) uit de dictionary en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4}
meubels = {'banken': 10, 'stoelen': 20}
# Opdracht 2a:
meubels['banken'] -= 6
print(meubels)  # Het resultaat is: {'banken': 4, 'stoelen': 20}
del meubels['stoelen']
print(meubels)


# Opdracht 2c:
# De winkel gaat tafels verkopen en koopt er gelijk 15 in. Voeg de naam 'tafels' toe met een waarde van 15 en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4, 'tafels': 15}
# ==========================================
meubels = {'banken': 10, 'stoelen': 20, 'tafels': 15}
# Opdracht 2a:
meubels['banken'] -= 6
print(meubels)  # Het resultaat is: {'banken': 4, 'stoelen': 20}
del meubels['stoelen']

print(meubels)

#==========================================
# Opdracht 3:
# Docent Erik heeft proefwerken van studenten nagekeken en de cijfers in een dictionary opgeslagen.
# Erik komt erachter dat hij een fout heeft gemaakt en moet de cijfers met een factor 1,5 vermenigvuldigen.
# Met als enige uitzondering dat een cijfer nooit hoger mag zijn dan een 10.
# Print de uitkomst om te zien of je het juiste resultaat krijgt.

# Gegeven is de dictionary 'cijfers' met daarin de keys 'Jaap', 'Winnie', 'Jeroen' en 'Lana' en hun cijfers.
# Verwachte uitkomst: {'Jaap': 4.5, 'Winnie': 6.0, 'Jeroen': 10, 'Lana': 10}
# ==========================================
#MIN =Voor elke naam en elk cijfer: maak een nieuw cijfer dat 1,5 keer zo hoog is, maar nooit hoger dan 10.
cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 8, 'Lana': 9}

nieuwe_cijfers = {naam: min(cijfer * 1.5, 10) for naam, cijfer in cijfers.items()}

print(nieuwe_cijfers)
#==========================================

cijfers_2026 = {'Eva': 5, 'Noah': 9, 'Liam': 7.5, 'Sara': 10, 'Mila': 8.2}
nieuwe_cijfers_Juf = {naam: min(cijfer + 2, 10) for naam, cijfer in cijfers_2026.items()}
print(nieuwe_cijfers_Juf)
#=============================================
prijzen = {'Tafel': 120, 'Stoel': 45, 'Kast': 300, 'Lamp': 25}
#30% korting op alles hoger wat hoger is  30 euro
nieuweprijzen = {
    product: prijs * 0.7 if prijs >= 30 else prijs
    for product, prijs in prijzen.items()}
print("de nieuwe prijzen met korting van 30 zijn: ", nieuweprijzen)

#=======================================================
prijzen = {'Tafel': 120, 'Stoel': 45, 'Kast': 300, 'Lamp': 25}

nieuwe_prijzen = {
    product: prijs * 0.8 if prijs >= 30 else prijs
    for product, prijs in prijzen.items()}

print(nieuwe_prijzen)



# ==========================================
# Opdracht 4:
# De eigenaar van dierentuin 'Het Zootje' heeft een lijst met dieren en hun aantallen. De dieren en hun aantallen zijn opgeslagen in een
# dictionary.
# Maak onderstaande deelopdrachten.
#================================================================
dierendatabase = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
for dier in sorted(dierendatabase.keys()):
    print(dier, dierendatabase[dier])


# Opdracht 4a:
# De eigenaar wil de dieren op alfabetische volgorde zien. Sorteer de dieren op naam en print de dictionary uit.
# Verwachte uitkomst: {'Aap': 5, 'Giraffe': 2, 'Leeuw': 3, 'Olifant': 4, 'Zebra': 1}
#
# Opdracht 4b:
# Nu wil de eigenaar in een oogopslag wat het hoogste aantal is en het laagste.
# Sorteer nu de aantallen van hoog naar laag en print de dictionary uit. (De keys hoef je niet te printen)
# ==========================================

dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
aantallen = sorted(dieren.values(), reverse=True)
print(aantallen)
