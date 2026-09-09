# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de
# variabelen num1, num2 en num3 (maak deze variabelen met inputs zelf aan).
# Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================

num1 = int(input("Voer een getal 1 in: "))
num2 = int(input("Voer een getal 2 in: "))
num3 = int(input("Voer een getal 3 in: "))

a = num1
b = num2
c = num3


if a > b:
    a,b = b,a
    if a > c:
        c,a = a,c
    if b > c:
        b,c = c,b
print(num1, num2, num3)

## TODO Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

