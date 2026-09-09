# Opgave 7:
# Begroeting op Basis van het Uur van de Dag
#
# Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9).
#VARIABEL  UUR = 9
# Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond".
# Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, (if uur < 12:

# zeg "Goedemorgen"; als het minder dan 18 is, zeg "Goedemiddag"; elif uur < 18:
# en anders, zeg "Goedenavond".
# Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn. Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.
#
# Check het resultaat met de print() methode. Veranderde de waarde van 'uur' om te zien of de begroeting verandert.
# ==========================================
uur = 8

if uur < 12:
    print("goedemorgen")
elif uur < 18:
    print("goedemiddag")
else:
    print("goedenavond")

