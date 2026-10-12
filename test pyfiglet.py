from pyfiglet import Figlet
f = Figlet(font='slant')
print()
print(f.renderText('f r a n k '
                   'is '
                   'gek'))
#---------------------------------------------------------hieronder begint rich

#PRETTY TABLE

tabel = PrettyTable()
tabel.field_names = ["Naam", "Leeftijd"]

tabel.add_row(["Jan", 20])
tabel.add_row(["Piet", 25])
print(tabel)

data = [
["Roulette", 15],
["Blackjack", 8]
]

print(tabulate(data, headers=["Spel", "Aantal keer"], tablefmt="grid"))