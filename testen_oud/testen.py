from datetime import datetime
# +++++++++++++++++++++++++++hieronder alle constante
TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18
# Programma verloop:
# 1. Vraag gebruikersgegevens op
# 2. Bepaal begroeting
# 3. Controleer leeftijd
# 4. Bereken saldo
# 5. Toon welkomsbericht
# 6. Start hoofdmenu


def main():
    print("===============  LET'S PLAY  ================")
#stap 1 vraag de gegevsn op
    name = input("Wat is je naam? ").capitalize()
    birthdate = input("Wat is je geboortedatum? (dd-mm-yyyy) ")
    gender = input("Wat is je gender? (m/v/x) ").strip().lower()
    startbudget = float(input("Hoeveel geld neem je mee naar Casino de Gouden Driehoek? € "))
#stap2 bepaal begroeting
    salutation = determine_salutation(name, gender)
#stap 3 controleer leeftijd
    age = check_age(birthdate)
#Als de gebruiker jonger is dan 18, stop het programma met return
    if age < MIN_AGE:
        print(f"\nSorry {salutation}, je moet 18 jaar of ouder zijn om deze applicatie te gebruiken.")
        return
#stap 4 Bereken de kosten en het saldo.
    total_costs = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
    balance = startbudget - total_costs
# controleer of er genoeg budget is
    if balance < 0:
        print("\nOnvoldoende budget om het casino te betreden.")
        print(f"Je komt €{-balance:.2f} tekort.")
        return
#stap 5Toon het welkomstbericht.
    show_welcome_message(startbudget, balance, salutation)
#stap 4 Start het menu
    show_main_menu(name, birthdate, salutation, balance)



#functie gemaakt voor leeftijdcheck
def check_age(birthdate):
    day, month, year = birthdate.split("-")
    age = 2026 - int(year)
    return age

#functie gemaakt voor bepalen begroeting
def determine_salutation(name, gender):
    if gender == "m":
        return f"meneer {name}"
    elif gender == "v":
        return f"mevrouw {name}"
    else:
        return f"speler {name}"

#functie gemaakt voor welkoms bericht
def show_welcome_message(startbudget, balance, salutation):
    total = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
    if balance < 0:
        print("\nOnvoldoende budget om het casino te betreden.")
        print(f"Je komt €{-balance:.2f} tekort.")
        return


    print("\nCasino de Gouden Driehoek")
    print("-" * 35)
    print(f"Welkom, {salutation}")
    print()
    print(f"Startbudget:    € {startbudget:.2f}")
    print(f"Vaste kosten:   € {total:.2f}")
    print(f"Saldo:          € {balance:.2f}")
    print()

def show_main_menu(name, birthdate, salutation, balance):
    while True:
        print("\n=== Hoofdmenu ===")
        print("1. Spellen")
        print("2. Saldo")
        print("3. Account")
        print("0. Stop")

        keuze = input("Maak een keuze: ")

        match keuze:
            case "1":
                show_games_menu(balance, salutation)
            case "2":
                show_balance(balance)
            case "3":
                show_account(name, birthdate, salutation)
            case "0":
                print("Programma wordt afgesloten...")
                break
            case _:
                print("Ongeldige keuze, probeer opnieuw.")


def show_games_menu(balance, salutation):
    while True:
        print("\n=== Spellen Menu ===")
        print("1. Fruitmachine")
        print("2. Roulette")
        print("0. Terug")

        keuze = input("Maak een keuze uit: ")

        match keuze:
            case "1":
                play_fruitmachine(balance, salutation)
            case "2":
                play_roulette(balance, salutation)
            case "0":
                break
            case _:
                print("Ongeldige keuze, probeer opnieuw.")


def play_fruitmachine(balance, salutation):
    print(f"\n{salutation}, de fruitmachine is nog niet geïmplementeerd.")
    print(f"Huidig saldo: €{balance:.2f}")


def play_roulette(balance, salutation):
    print(f"\n{salutation}, roulette is nog niet geïmplementeerd.")
    print(f"Huidig saldo: €{balance:.2f}")


def show_balance(balance):
    print(f"\nJe huidige saldo is: €{balance:.2f}")


def show_account(name, birthdate, salutation):
    print("\n=== Accountgegevens ===")
    print(f"Naam: {salutation}")
    print(f"Geboortedatum: {birthdate}")
main()