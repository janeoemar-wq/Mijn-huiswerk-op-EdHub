from idlelib.run import handle_tk_events

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

nummers = [2, 5, 7, 11, 15]
print(nummers[0] + nummers[1])
print(nummers[2] * nummers[3]) # 7x11
som = (nummers)
print(sum(nummers))

#REMOVE
tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]
tafel_van_drie.remove (32)    #(hier 32 invullen, tussen aanhalingstekens)
print(tafel_van_drie)

#WIJZIG
tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]
tafel_van_drie[4] = 15   #hier vierkante haken met daarin de plek invullen
print(tafel_van_drie)

#TOEVOEGEN AAN EIND
tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]
tafel_van_drie.append(30)
print(tafel_van_drie)

#INSERT
tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]
tafel_van_drie.insert(8, 21)
print(tafel_van_drie)

