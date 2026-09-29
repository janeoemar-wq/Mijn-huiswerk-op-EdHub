#tensor
tensor = [[[1, 2],[3, 4]],[[5, 6],[7, 8]]]
print(tensor[0][1][1])

# ONDERSTAANDE IS HETZELFDE ALLEEN ZICHTBAAR OP WELKE HOOGTE WELKE LIJSTEN WAARBIJ
# HOREN
tensor = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
print(tensor[0][1][1])


getal = int(input('getal = '))
aantal = 0

for teller in range(1, getal+1, 1) :
    if getal % teller == 0 :
        aantal += 1

if aantal == 2 :
    print("priemgetal")
else :
    print("geen priemgetal")