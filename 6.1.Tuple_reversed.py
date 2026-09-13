# ==========================================
# Voorbeeld opdracht:
# Declareer twee tuples met de namen ‘tuple_een’ en ‘tuple_twee’.
# tuple_een krijgt de waarden 1, 2 en 3. tuple_twee krijgt de waarden 4, 5 en 6.
# Zorg dat je een tuple krijgt met de waarden 1, 2, 3, 4, 5 en 6. Onthoud dat tuples onveranderlijk zijn.
# ==========================================

tuple_een = (1, 2, 3)
tuple_twee = (4, 5, 6)
samen = tuple_een + tuple_twee
print(samen)

# je zal een nieuwe tuple variabele moeten declareren. De tuples die al gedeclareerd zijn kunnen niet worden
# aangepast
# (zoals een list kan worden aangepast met append, insert en remove).
#combined_tuple = tuple_een + tuple_twee
#print('combined tuple: ', combined_tuple)  # Het resultaat is: (1, 2, 3, 4, 5, 6

tuple_een = (1, 2, 3)
tuple_twee = (4, 5, 6)
combined_tuple = tuple_een + tuple_twee
print(" combined tuple:", combined_tuple)

# ==========================================
# Opdracht 1:
# maak een tuple aan met de waarden 'b', 'c', 'a'
# print de waarden van de tuple in de alfabetische volgorde (a, b, c)
# Tip: maak gebruik van de indexen van de tuple
#
# Verwachte uitkomst:  a b c
# ==========================================
tuple = ('b', 'c', 'a')
print (tuple [2], tuple [0], tuple [1])

# ==========================================
# Opdracht 2:
# Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 1 tot en met 5 waarin elk element bestaat uit
# een tuple die het getal en het bijbehorende kwadraat bevat.
# Gebruik een list comprehension.
#
# Verwachte uitkomst: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
getal_kwadraat_paar = [(getal, getal * getal) for getal in range (1,11)]
print(getal_kwadraat_paar)

getal_kwadraat_paar = [(getal, getal * getal) for getal in range(2, 9)]
print(getal_kwadraat_paar)

# =========================================
# Opdracht 3:
# Maak een tuple genaamd tuple_count met de waarden 1, 2, 3, 4, 5
# Draai de volgorde van de getallen om. Zorg dat je een nieuwe tuple krijgt met de waarden 5, 4, 3, 2, 1
# Tip: Maak gebruik van de reversed() functie
#
# Verwachte uitkomst: (5, 4, 3, 2, 1)
# ==========================================
tuples_count = (1, 2, 3, 4, 5)
tuples_omgekeerd = tuples(reversed(tuples_count))
print(tuples_omgekeerd)