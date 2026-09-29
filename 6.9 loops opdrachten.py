# # Tafels
#
# # Schrijf een programma dat de tafel van een getal afdrukt.
# # De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# # De tafel van 7 ziet er bijvoorbeeld als volgt uit:
#MET LOOP
getal = int(input("Voer een getal in waar je de tafel van wilt zien: "))
for tafel in range(1, 11):
    print(tafel, "x", getal, "=", tafel * getal)

# # Probeer het eerst zonder loop,
getal = int(input("Voer een getal in waar je de tafel van wilt zien: "))
print(1, "x", getal, "=", 1 * getal)
print(2, "x", getal, "=", 2 * getal)
print(3, "x", getal, "=", 4 * getal)
print(4, "x", getal, "=", 4 * getal)
print(5, "x", getal, "=", 5 * getal)
print(6, "x", getal, "=", 6 * getal)
print(7, "x", getal, "=", 7 * getal)
print(8, "x", getal, "=", 8 * getal)
print(9, "x", getal, "=", 9 * getal)
print(10, "x", getal, "=", 10 * getal)
## # --------------------------------------------------------------------------------------------
#
# # Optellen
# # Schrijf een programma dat de som van alle getallen
# tot een bepaalde limiet berekent.
limiet  = int(input("Voer een limiet in: "))
som = 0
for getal in range(1, limiet+1):
    som = som + getal
print("De som is:", som)


# # Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)
# # --------------------------------------------------------------------------------------------
#
# # Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# # FizzBuzz
#
# # Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# # Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# # En voor veelvouden van vijf, druk "Buzz" af.
# # Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.
#
#
#
# # --------------------------------------------------------------------------------------------
#
#
# # Fibonacci-reeks
#
# # De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# # Elk volgend getal is de som van de twee voorgaande.
# # De eerste 10 getallen van de Fibonacci-reeks zijn:
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# # 0 + 1 = 1
# # 1 + 1 = 2
# # 1 + 2 = 3
# # 2 + 3 = 5
# # 3 + 5 = 8
# # 5 + 8 = 13
# # 8 + 13 = 21
# # 13 + 21 = 34
#
# i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))
#
# # De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
# a = 0
# b = 1
#
# # Eerst drukken we de eerste twee getallen af
#
#
# # Vervolgens berekenen we de volgende getallen en drukken ze af