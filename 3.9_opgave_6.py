# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’)    # dit is een float
#
# b. print(float(12))        # goed
#
# c. print(int('1plus1'))   # in een int kunnen geen letters
#
# d. print(str(25E10))    # goed E10 = 10 tot de macht 10   -
                              #  25E10 = 25 × 10.000.000.000
# ==========================================
print(float("1490.99"))

print(float(12))
print(str(25E10))
