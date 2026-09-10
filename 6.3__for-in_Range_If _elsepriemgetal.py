
getal = int(input('getal = '))
aantal = 0

for teller in range(1, getal+1, 1) :
    if getal % teller == 0 :
        aantal += 1

if aantal == 2 :
    print("priemgetal")
else :
    print("geen priemgetal")

