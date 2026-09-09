# ==========================================
# Opgave 2:
# Hoe schrijf je de volgende getallen uit in de wetenschappelijke notatie van Python?
# print de getallen.

#     -12.000.000

getal = int(-1.2e7)
print("getal: ", getal)
#===================================================================
#     0.13 met drie extra nullen (0.00013)
#     #Verplaats de komma totdat je een getal tussen 1 en 10 krijgt: 0.00013 → 1.3
# Je hebt de komma 4 plaatsen naar rechts verplaatst → exponent wordt –4.
# Dus: 0.00013
# = 1.3 × 10−4

getal = 1.3e-4
print("getal: ", getal)

#======================================================================
#     64.000.000.000
# ==========================================

getal = int(64e7)
print("getal: ", getal)