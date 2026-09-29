# Uber applicatie V1.0 🚗

# -----------------------------
# Functie: diensten + prijzen
# -----------------------------
def get_services():
    return {
        "1": ("uber black, 2.22"),
        "2": ("uber white, 3.33"),
        "3": ("uber red, 4,44")}

#-----------------------------
# Functie: keuze gebruiker
# -----------------------------
def get_user_choice():
    services = get_services()

    print("Kies het type Uber:")
    print("1. Uber Black 🙂")
    print("2. Uber Van 🚐")
    print("3. Uber X 🚗")
    print("-------------------")
    while True:
        choice = input("Voer het nummer van uw keuze in: ")
        if choice in services:
               return choice
        print("Ongeldige keuze 😕 probeer opnieuw.")


# -----------------------------
# Functie: kilometers vragen
# -----------------------------
def get_kilometers():
    while True:
        km = input("Voer het aantal kilometers van uw rit in: ")
        if km.isdigit():
            return int(km)
        print("Voer een geldig nummer in 🙃")


# -----------------------------
# Functie: kosten berekenen
# -----------------------------
def calculate_cost(price_per_km, km):
    return price_per_km * km


# -----------------------------
# MAIN functie
# -----------------------------
def main():
    print("Welkom bij de Uber applicatie! 🚗🙂\n")

    choice = get_user_choice()
    km = get_kilometers()

    services = get_services()
    service_name, price = services[choice]

    total_cost = calculate_cost(price, km)

    print()
    print(f"U heeft gekozen voor {service_name}. 👍")
    print(f"De kosten voor uw rit van {km} kilometer(s) zijn €{total_cost:.2f}. 💶")
    print("Bedankt voor het gebruiken van onze dienst! 😊")


# -----------------------------
# Programma starten
# -----------------------------
main()