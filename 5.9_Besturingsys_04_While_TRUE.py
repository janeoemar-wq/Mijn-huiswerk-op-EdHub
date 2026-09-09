# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0. Schrijf een programma dat herhaaldelijk een getal als input vraagt.
# Elk getal dat je invoert moet moet worden opgeteld bij het totaal.
# Als je 0 invoert moet het programma stoppen en
# met een print statement het totaal
         # en het gemiddelde van de getallen afdrukken (dus totaal / aantal inputs).
# Als er geen getallen zijn ingevoerd moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================

totaal = 0
aantal = 0
while True:
    getal = float(input("Geeft een getal in (0 om te stoppen) "))
    if getal == 0:
        break
    totaal+= getal
    aantal += 1
if aantal == 0:
    print("er zijn geen getallen ingevoerd!")
else:
    gemiddelde = totaal / aantal
    print("totaal", totaal)
    print("gemiddelde", gemiddelde)



