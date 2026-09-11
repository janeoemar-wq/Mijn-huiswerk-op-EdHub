# maand = list(range(1, 31))
#
# x = int(input("Welke dag wil je zien? Kies 0 voor zondag, 1 voor maandag, etc"))%7
# dagen = maand[x::7]
# print(dagen)
#
# jaar = list(range(1, 13))
#=====================================================
#Print de eerste 3 namen
lijst_namen = 'Alfred', 'Bob', 'Annelien', 'David', 'Erik'
print(lijst_namen[:3])

#Vervang David en Erik door ['Daphne', 'Eva', 'Frederique'] en print de uitkomst
lijst_namen = ['Alfred', 'Bob', 'Annelien', 'David', 'Erik']
lijst_namen[3:5] = ['Daphne', 'Eva', 'Frederique']
print(lijst_namen)

lijst1 = ["banaan", "appel", "peer"]
lijst2 = lijst1
lijst1.append("Jane")
print(lijst2)

lijst3 =  ["tafel", "bank", "stoel"]
lijst4 = lijst3
lijst3.append(['banaan', 'appel', 'peer', 'kers'])
print(lijst4)

