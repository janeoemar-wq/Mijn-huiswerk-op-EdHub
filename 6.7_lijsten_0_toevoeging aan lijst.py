# ==========================================
# Voorbeeld Opdracht
# Maak een lijst aan met daarin de volgende getallen: 10, 20 en 30
#
# Voer de volgende opdrachten uit:
# - Voeg het getal 40 toe aan (het einde van) de lijst
#
# Aan het einde print je de lijst 'getallen'.
# ==========================================


# list met getallen
getallen = [10, 20, 30]

# Voeg het getal 40 toe aan (het einde van) de lijst
getallen.append(40)
print('list na toevoeging 40 aan het einde van de lijst: ', getallen)  # Het resultaat is: [10, 20, 30, 40]
#TODO .append nog even nalezen in edhup

getallen = [1, 2, 3, 4, 5]
getallen.append(6)
print('lijst na toevoeging 6 aan het einde van de lijst: ', getallen)


nummers = [2, 5, 7, 11, 15]
print(nummers[0] + nummers[1])
print(nummers[2] * nummers[3]) # 7x11
som = (nummers)
print(sum(nummers))

geschiedenis = [
    "http://mijnsite.nl/home",
    "http://mijnsite.nl/producten",
    "http://mijnsite.nl/product_detail"
]

# Gebruiker bezoekt een nieuwe pagina
geschiedenis.append("http://mijnsite.nl/winkelwagen")

print("Geschiedenis 1:", geschiedenis)

# Gebruiker klikt op 'terug'
verwijderde_pagina = geschiedenis.pop()

print("Terug naar:", geschiedenis[-1])
print("Verwijderde pagina:", verwijderde_pagina)
print("Geschiedenis 2:", geschiedenis)

#kleuren.pop(1) # verwijderen op index
#kleuren.remove("geel") # verwijderen op waarde
#Meer regels weergeven

#Ezelsbruggetje: .pop() = haal iets eruit en geef het verwijderde item terug.