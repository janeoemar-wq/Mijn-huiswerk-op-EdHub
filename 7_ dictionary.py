#Twee woordenboeken zijn gelijk als ze precies dezelfde sleutel-waarde paren bevatten,
# waarbij die paren niet in dezelfde volgorde hoeven te staan.
# We kunnen dit testen met behulp van ‘==’.
vakken1 = {'Python':10, 'Java':8, 'C#':5}
vakken2 = {'Java':8, 'C#':5, 'Python':10}

print(vakken1 == vakken2)   #true

#===============================================
# controleren met IN en NOT IN (true en false)
vakken = {'Python':10, 'Java':8, 'C#':5}

print('Python', 'Python' in vakken)     #Python True
print('SQL', 'SQL' in vakken)           # SQL False
print('Pascal', 'Pascal' not in vakken)   #Pascal True
print('aantal paren:', len(vakken))       #aantal paren opvragen met len

#===================================================================
vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6}
# GET als het wel/ niet voorkomt
print(vakken.get('Pascal', 'Pascal staat niet in het woordenboek')) #output: Pascal staat niet in het woordenboek
print(vakken.get('Java', 'Java staat niet in het woordenboek'))   #output :8

#================================================================
#Als we alle vakken willen afdrukken waarvan de waarde minstens 6 is kan dat met de volgende code/
# met de methodes: .items()

for vak,aantal in vakken.items() :

    if aantal >= 6 :

        print(vak, '->', aantal)
#=====================================================================
vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6, 'Pascal': 4}

for vak in sorted(vakken.keys()) :

    print(vak, end=' ')
#=====================================

vakken = {'Python':10, 'Java':8, 'C#':5, 'SQL':6}

vakken_view = vakken.keys()

print(vakken_view)

vakken['Pascal'] = 4

print(vakken_view)

#omzetten van woordenboek naar lijst

vakken = {'Python':10, 'Java':8, 'C#':5, 'SQL':6}

vakkenlijst = list(vakken.keys())

print(type(vakkenlijst), vakkenlijst)

#====================================
cijfers = {'Jan': [7.3, 8.5, 6.4], 'Piet': [6.9, 7.2, 9.1, 8.1]}

gemiddelde_cijfers = {s : sum(w) / len(w) for s, w in cijfers.items()}

print(gemiddelde_cijfers)


cijfers = {'Jan': [7.3, 8.5, 6.4], 'Piet': [6.9, 7.2, 9.1, 8.1]}

gemiddelde_cijfers = {s : sum(w) / len(w) for s, w in cijfers.items()}

print(gemiddelde_cijfers)

print({ s : f"{(sum(w) / len(w)):.2f}" for s, w in cijfers.items() })


#=================
import random
import timeit

getallist = list(getal*10 for getal in range(100_000))
getaldict = {getal*10 : 0 for getal in range(100_000)}

zoekgetal = random.randrange(1_000_000)

starttime = timeit.default_timer()
if zoekgetal in getallist :
    print('gevonden in lijst')
else :
    print('niet gevonden in lijst')
print("zoektijd in de lijst :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
if zoekgetal in getaldict :
    print('gevonden in woordenboek')
else :
    print('niet gevonden in woordenboek')
print("zoektijd in het woordenboek :", timeit.default_timer() - starttime)

getallist = list(getal * 10 for getal in range(100_000))
print(type(getallist), getallist)