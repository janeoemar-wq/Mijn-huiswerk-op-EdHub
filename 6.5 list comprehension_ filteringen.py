#dit zijn filteringen
lijst5 = [getal for getal in range(1,21) if getal not in (3,5,7)]
print(lijst5)

overzicht =[nr for nr in range(1,11) if nr not in (2, 4,6)]
print(overzicht)


gebruikers = ["jan@example.com", "piet",    "klaas@example.com","test", "admin.example.com"]

emails = [xx for xx in gebruikers if "@" in xx]
#of
emails = [ll for ll in gebruikers if "com" in ll]

print(emails)

lijst5 = [getal for getal in range(1,21) if getal % 2 ==0]
print(lijst5)

