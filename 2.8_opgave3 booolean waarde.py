# ==========================================
# Opgave 3
# Gegeven is x = 5 en y = -5
# Gebruik logische operatoren om te controleren of de variabelen positief zijn en kleiner dan 10.
# Print het resultaat als boolean waarde.
#
# Verwachte uitkomst voor x is: True
# Verwachte uitkomst voor y is: False
# ==========================================
from operator import and_

x = 5
y = -5
resultaatx = (x > 0) and (x < 10)
resultaaty = (y > 0) and (y < 10)

print(resultaatx)
print(resultaaty)


