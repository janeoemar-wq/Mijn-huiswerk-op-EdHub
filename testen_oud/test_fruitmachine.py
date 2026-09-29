import random

def start(balance):
    print("=== Winregels Fruitmachine ===")
    print("→ Grote prijs (3x inzet) 🍒🍒🍒 | 🍋🍋🍋 | ⭐⭐⭐")
    print("→ Kleine prijs (inzet terug) 🍒🍒❓ | 🍋❓🍋 | ⭐❓⭐")
    print("→ Geen prijs (inzet kwijt) 🍒🍋⭐")
    print("==============================")

    while True:
        balance = play_fruitmachine(balance)
        if balance <= 0:
            print("Je saldo is op.")
            break
        opnieuw = input("Nog een keer spelen? (ja/nee): ")
        if opnieuw.lower() == "nee":
            break

    return balance

symbolen = ["kers", "citroen", "ster"]
emojij_lijst = {
    "kers": "🍒",
    "citroen": "🍋",
    "ster": "⭐"}

def play_fruitmachine(balance):
    print(f"Je huidige saldo is €{balance:.2f}")
    inzet = float(input("Wat wil je inzetten? €"))
    if inzet > balance:
        print("Onvoldoende saldo!")
        return balance
    balance -= inzet

    # inzet valideren
    if inzet <= 0:
        print("Inzet moet hoger zijn dan 0.")
        return balance

    if inzet > balance:
        print("Je hebt niet genoeg saldo.")
        return balance

    # rollen draaien
    def trek_hendel():
        return [random.choice(symbolen) for _ in range(3)]
    rol1 = random.choice(symbolen)
    rol2 = random.choice(symbolen)
    rol3 = random.choice(symbolen)

    print(f"\n | {emojij_lijst[rol1]}  {rol1}| {emojij_lijst[rol2]} {rol2} | {emojij_lijst[rol3]} {rol3}|")

      # prijs bepalen
    if rol1 == rol2 == rol3:
        print()
        print("Grote prijs! Je wint 3x je inzet.")
        balance += inzet * 3
    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        print()
        print("Kleine prijs! Je krijgt je inzet terug.")
        balance += inzet
        # inzet terug → balance blijft gelijk
    else:
        print()
        print("Helaas geen prijs. Je verliest je inzet.")

    print(f"Nieuwe balance: €{balance}")
    return balance
