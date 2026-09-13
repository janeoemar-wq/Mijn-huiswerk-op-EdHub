# ==========================================
# Voorbeeld Opdracht
# Maak een lijst aan met daarin de volgende getallen: 10, 20 en 30
#
# Voer de volgende opdrachten uit:
# - Voeg het getal 40 toe aan (het einde van) de lijst
#
# Aan het einde print je de lijst 'getallen'.
# ==========================================

nummer = [10, 20, 30]
nummer.append(40)
print(nummer)


# ==========================================
# Opdracht 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen:
# 1, 1, 2, 3, 5, 8 enzovoorts
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibonacci’
# die een lijst als parameter meekrijgt.
# Voer de volgende opdrachten uit:
# - Maak een variabele aan genaamd 'fibonacci_start_reeks' en geef  die de eerste twee elementen
# van de Fibonacci reeks.
# - Maak een functie genaamd fibonacci die de fibonacci_reeks uitbreidt met een nieuw element.
# - Roep de functie 5 keer aan (Bijvoorbeeld met een for-loop).
# - Print de waarde van de fibonacci_reeks
#
# Verwachte uitkomst:   [1, 1, 2, 3, 5, 8, 13]
# ==========================================

#variabele maken
fibonacci_start_reeks = [8, 1]
print(fibonacci_start_reeks)

#functie maken
def fibonacci(fibonacci_reeks):
    nieuw_getal = fibonacci_reeks[-1] + fibonacci_reeks[-2]
    fibonacci_reeks.append(nieuw_getal)
    print(fibonacci_reeks)

# Roep de functie 5 keer aan
for i in range(5):
    fibonacci(fibonacci_start_reeks)
    print(fibonacci_start_reeks)

# ==========================================
# Opdracht 3:
# Maak een lijst ‘kwadraten’ die de kwadraten bevat van de getallen
# 1 tot en met 10. Gebruik een for loop.
#
# Verwachte uitkomst:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ===========
kwadraten = []
for getal in range(1, 11):
    kwadraten.append(getal * getal)
print(kwadraten)