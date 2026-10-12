# Week 3: Casino de Gouden Driehoek: hoofdmenu, functies en fruitmachine
## Inleiding
Vorige week heb je roulette gebouwd en gecontroleerd of spelers oud genoeg zijn om verder te spelen. Deze week bouw je daar op verder met functies. Je gaat de applicatie van vorige week ombouwen zodat het een hoofdmenu heeft en je gaat de spellen in een aparte games/-map zetten, waaronder ook een nieuw spel, de fruitmachine.

Een fruitmachine is een spel waarbij je 3 rollen laat draaien door een hendel over te halen. Wanneer de rollen stoppen met draaien, laten ze drie plaatjes zien. Als dit drie dezelfde plaatjes zijn, verdien je drie keer je inzet, als twee plaatjes hetzelfde zijn, krijg je je inzet terug, en als het drie verschillende plaatjes zijn, verlies je je inzet.

## Spelregels
De spelregels van een fruitmachine zijn heel simpel:

De machine heeft 3 posities (slots, vandaar dat dit ook wel "slotmachine" wordt genoemd).
Elke positie heeft een plaatje, bijvoorbeeld een ster, een maan en of een zon.
Bij start van het spel, haal je een virtuele hendel over en wordt er een willekeurig plaatje gekozen voor elke van de drie posities.
Heb je uiteindelijk 2 of 3 dezelfde plaatjes, dan heb je prijs. Zo niet, dan heb je niks gewonnen.
# Opdracht beschrijving
Je gaat de code van vorige week opsplitsen in functies. Maak onder andere de volgende functies:

main()
check_age(birthdate)
determine_salutation(name, gender)
show_welcome_message(startbudget, balance, salutation)
Daarnaast komen daar nog meer functies bij, zoals:

show_main_menu()
show_games_menu()
play_fruitmachine(balance, salutation)
play_roulette(balance, salutation)
show_balance(balance)
show_account(name, birthdate, salutation)
check_age
Deze functie implementeer je zodat het om de input van de birthdate kan: birthdate = check_age(input("Wat is je geboortedatum? (dd-mm-yyyy) ")). Deze functie doet dus de leeftijdscheck die je vorige week hebt gemaakt. Als die leeftijdscheck faalt, exit de applicatie. Als de leeftijdscheck slaagt, moet je zorgen dat de geboortedatum (die je als parameter binnen krijgt vanuit de input) weer wordt geretourneerd. Die moet je immers nog opslaan in de birthdate variabele.

Het is handig om het berekenen van de leeftijd in een aparte calculate_age(birthdate) functie te zetten, omdat je de leeftijd later nog eens nodig hebt.

### determine_salutation
Deze functie ontvangt een naam en een geslacht. Het retourneert de gemaakte begroeting als string.

### show_welcome_message
Deze functie verwerkt de printout die je in de eerste week al gemaakt had.

### main
De main functie bevat de belangrijkste logica van de applicatie. Net als in het script van vorige week, begin je in de main functie ook met het opvragen van input van de gebruiker. Denk hierbij aan de leeftijdscheck. Vervolgens bereken je de salutation, de balance en laat je het welkomstbericht zien. Vervolgens start je de while True loop, maar daarin start je niet het roulettespel, maar het hoofdmenu.

# hoofdmenu
Het hoofdmenu staat in een while True loop in de main functie. Het heeft vier opties:

1 Spellen
2 Saldo
3 Account
0 Stop
Implementeer dit met een if/elif/else constructie of een match statement.

## spellen
De "spellen" optie van het hoofdmenu leidt tot een submenu met (voor nu) de volgende opties:

1 Fruitmachine
2 Roulette
0 Terug
Implementeer dit met een if/elif/else constructie of een match statement.

Alle spellen staan geïmplementeerd in de games package en elk spel heeft zijn eigen play-functie. Als de gebruiker voor fruitmachine kiest, roep je play_fruitmachines(balance) aan. Als de gebruiker voor roulette kiest, roep je play_roulette(balance) aan. Deze beide functies retourneren de nieuwe balance van de speler, zodat je de balance variabele kunt updaten.

### saldo
De saldo-optie laat de huidige balance van de gebruiker zien. Dit kan een simpele print zijn als print(f"Huidig saldo: € {balance:.2f}"), maar het staat wel in een eigen show_balance-functie. Optioneel kun je hier nog een introductieregel aan toevoegen die laat zien welke functie is aangeroepen.

### account
Net als de saldo-functionaliteit, print deze functionaliteit enkel een paar gegevens:

### naam
aanspreekvorm
geboortedatum
leeftijd (gebruik de calculate_age functie, als je die hebt)
Optioneel kun je ook bij deze functionaliteit weer een korte, inleidende regel printen om te laten zien welke functionaliteit is aangeroepen.

## roulette
Het roulettespel heb je vorige week al uitgewerkt. Nu is het je taak om dit in logische functies te verdelen en naar de games package te verplaatsen in een eigen roulette.py module.

Refactor de code, zodat het gebruik maakt van logische functies. Denk bijvoorbeeld aan functies voor de volgende functionaliteiten:

Het printen van de opties (rood, zwart, even, oneven) die de gebruiker kan kiezen.
Bepalen of de gebruiker gewonnen of verloren heeft.
De gebruiker om de gewenste inzet vragen en dit valideren.
Een main functie (misschien met een meer passende naam, zoals play_roulette) waar alles aan elkaar geknoopt wordt en de while-loop draait.
Zorg dat de play_roulette functie de balance vanuit de main module ontvangt en de nieuwe balance weer retourneert.

## fruitmachine
De globale functionaliteit van de fruitmachine heeft veel overeenkomsten met die van het roulettespel. De specifieke functionaliteit van het spel, is natuurlijk wel iets anders:

Werk tenminste met een play_fruitmachine(balance) functie.
Zorg dat de gebruiker een geldbedrag kan inzetten. Dit moet wel een geldig bedrag zijn en binnen het budget passen.
Speel het spel door drie waardes te bepalen, bijvoorbeeld "kers", "citroen" en "ster".
Bepaal of de speler gewonnen heeft. Bij drie dezelfde symbolen heeft de gebruiker een grote prijs gewonnen, bij twee dezelfde symbolen een kleine prijs en bij drie verschillende symbolen is er geen prijs.
Bereken de nieuwe balance en retourneer dit naar de main module.
### Voorbeeld output:
Hieronder zie je een voorbeeld van de output die je applicatie kan geven. Jouw implementatie hoeft niet exact zo te verlopen, maar schetst een beeld van de beoogde oplossing.

Wat is je naam? Jansen
Wat is je geboortedatum? (dd-mm-yyyy) 12-09-1984
Wat is je gender? (m/v/x) m
Met hoeveel geld begin je in Casino de Gouden Driehoek? € 300

Casino de Gouden Driehoek
-----------------------------------
Welkom, meneer Jansen

Startbudget:    € 300.00
Vaste kosten:   € 16.50
Saldo:          € 283.50

Je hebt nog genoeg budget voor toegang tot het casino.

Casino de Gouden Driehoek - hoofdmenu
-------------------------------------
1. Spellen
2. Saldo
3. Account
0. Stop

Kies een optie: 1

Casino de Gouden Driehoek - spellen
-----------------------------------
1. Fruitmachine
2. Roulette
0. Terug

Kies een spel: 1

Casino de Gouden Driehoek - fruitmachine
-----------------------------------
Huidig saldo: € 283.50
Druk op enter om te spelen of typ stop om terug te gaan: 
Hoeveel wil je inzetten? € 20
Rollen: kers | citroen | ster
Geen match. Je verliest € 20.00
Nieuw saldo: € 263.50

Casino de Gouden Driehoek - fruitmachine
-----------------------------------
Huidig saldo: € 263.50
Druk op enter om te spelen of typ stop om terug te gaan: stop

Casino de Gouden Driehoek - hoofdmenu
-------------------------------------
1. Spellen
2. Saldo
3. Account
0. Stop

Kies een optie: 0
Eindsaldo: € 263.50

Process finished with exit code 0
# Randvoorwaarden
Je main.py bevat minimaal 3 functies en 2 imports.
Je gebruikt diverse functies met een parameter en een returnwaarde.
Je gebruikt input() voor het hoofdmenu en voor de inzet van de fruitmachine of roulette.
Je berekent de inzet in een eigen functie en een eigen while-loop.
Je laat het saldo door de functies heen aanpassen.
Je gebruikt de leeftijdscheck uit week 2 in een eigen functie.
Je maakt ten minste 3 aparte bestanden: games/fruitmachine.py, games/roulette.py en main.py.
## Stappenplan
Let op: probeer deze opdracht eerst zelf op te lossen. Pas als dat niet lukt, mag je het stappenplan gebruiken.

Neem de gegevens uit week 1 mee en hergebruik de leeftijdscontrole en vaste kosten uit week 2.
Maak eerst een functie die het hoofdmenu toont met de opties spellen, saldo, account en stop.
Implementeer de helper functies. Hergebruik de code die je vorige week geschreven hebt.
Maak in de map games/ aparte bestanden fruitmachine.py en roulette.py.
Refactor de code in roulette.py, zodat het gebruik maakt van functies. 

Je kunt de volgende functies maken:
show_roulette_options() - Hier print je de opties (rood, zwart, even, oneven) die de gebruiker kan kiezen. Gebruik de print statements zoals je die vorige week hebt gedefinieerd.
determine_win(choice, color, odd_even) - Hier voer je het if/elif statement uit dat bepaald of de gebruiker gewonnen heeft of niet. Laat de functie True of False retourneren. In het if-statement zijn choice, color en odd_even de belangrijke variabelen, daarom geef je die als parameters mee aan de functie.
ask_for_bet(balance) - In deze functie zet je de input en de validatie logica om de inzet van de gebruiker te bepalen. Zet alles in een while True loop. Wanneer de gebruiker een verkeerd nummer ingeeft (lager dan 0 of lager dan het saldo), dan mag de gebruiker het direct opnieuw proberen. Als de gebruiker wel een goede inzet (stake) invult, dan mag je die stake retourneren.
play_roulette(balance) - Deze functie knoopt alles aan elkaar. Het bevat dezelfde logica als de roulette logica van vorige week, alleen zijn een paar onderdelen geëxtraheerd in helper functies. Vergeet ook niet om de round_number te definiëren vóór de while-loop.
Aan het eind van de play_roulette functie, retourneer je de nieuwe balance.
### Implementeer in fruitmachine.py de fruitmachine functionaliteit als volgt:
Definieer als eerst de play_fruitmachine(balance) functie.

Daarin definieer je een variabele: round_number = 1.

Daarna start je een while True loop.

Print als eerst een korte welkomsttekst, waarin je laat zien welk spel gespeeld wordt en wat je huidige saldo is.

Vraag daarna of de speler het spel wil spelen of wil stoppen.

Als de speler wil stoppen, return je de huidige balance.

Als de speler wil spelen, vraag je om diens inzet. Hiervoor kun je dezelfde ask_bet functie gebruiken als in het roulettespel. Merk op dat je nu twee keer ask_bet definieert en dat is niet DRY. Optioneel zou je nu een extra helper bestand kunnen maken waarin je ask_for_bet zet, zodat je die vanuit hier kunt aanroepen in zowel de fruitmachine, als de roulette.

Haal de stake (inzet) van de balance (saldo) af.

Zodra je de inzet hebt ontvangen, start je het spel.

Om het spel te spelen, moet je de waarde van elke rol bepalen. 
Schrijf dit in een eigen functie determine_rolls(round_number). 
De opties kunnen zijn citroen, kers of ster. 
Er zijn maximaal 9 mogelijke combinaties, maar je hoeft ze niet alle 9 te gebruiken. 
Als je alle 9 opties uitwerkt, gebruik je round_numer % 9 om je willekeurige waarde te bepalen. 
Stel je werkt 5 opties uit, dan gebruik je round_number % 5. Voor 5 opties zou je het volgende kunnen doen:

return "kers", "citroen", "ster"
return "kers", "kers", "kers"
return "ster", "ster", "citroen"
return "citroen", "kers", "ster"
return "ster", "ster", "ster"
Let op dat je drie strings retourneert. Je roept de functie dan ook als volgt aan: rol1, rol2, rol3 = determine_rolls(round_number)

Print de drie rollen die je hebt gedraaid.

Bepaal of de gebruiker heeft gewonnen met een determine_payout(rol1, rol2, rol3, inzet) functie. Als alle rollen hetzelfde zijn, krijgt de gebruiker drie keer de inzet terug. Als twee van de drie rollen gelijk zijn, krijgt de gebruiker één keer de inzet terug. Retourneer deze waarde en sla deze op in een payout variabele.

Als de payout groter is dan 0, tel je deze waarde bij de balance op en laat je de gebruiker weten wat deze heeft gewonnen. Optioneel kun je de gebruiker ook nog laten weten of het drie-op-een-rij was of slechts twee. Als de payout 0 (of minder) is, dan laat je de gebruiker weten dat deze verloren heeft.

Als laatste stap print je het huidige saldo en verhoog je round_numer met 1.

Roep vanuit het hoofdmenu de spellen aan als de speler dat spel in het spellen menu kiest. Gebruik hiervoor een if/else statement of een match statement.
Zorg dat het saldo na elke ronde wordt bijgewerkt en zichtbaar blijft in het hoofdmenu.
# Bonus
Zorg dat alle functies goede, duidelijke docstrings hebben.
Zorg dat total_cost als constante in de applicatie staat en vanuit daar gebruikt wordt.