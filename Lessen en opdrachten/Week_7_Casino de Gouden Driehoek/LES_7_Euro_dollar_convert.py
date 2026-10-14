"""
# geregistreerd: j....@hotmail/ ww oxxxx-1xx
MIJN_API_KEY = "62bfe84194efe62a3b19036b"
import requests


#Maak een functie met een parameter die de koers ophaalt vanuit de API:
def get_eur_to_usd_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
    response = requests.get(url) # GET REQUEST

    if response.status_code == 200:
        data = response.json()

        if "USD" in data["conversion_rates"]:
            return data["conversion_rates"]["USD"]
        else:
            print("Fout: USD wisselkoers niet gevonden.")
            return None
    else:
        print(f"Fout: {response.status_code} - {response.text}")
        return None
# amount = bedrag in euro's
# exchange_rate = wisselkoers van euro naar dollar
# return geeft het omgerekende bedrag terug

def convert_eur_to_usd(amount, exchange_rate):
    return amount * exchange_rate

def main():
    api_key = MIJN_API_KEY

    eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
    print()
    exchange_rate = get_eur_to_usd_rate(api_key)

    if exchange_rate is None:
        print("Wisselkoers kon niet worden opgehaald.")
        return

    usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)
    print(
        f"{eur_amount} EUR is gelijk aan {usd_amount:.2f} USD\n"
        f"(Wisselkoers: 1 EUR = {exchange_rate}USD)"

    )

main()
"""
"""
#-------------------nu met panel en tabel
# geregistreerd: j....@hotmail/ ww oxxxx-1xx
MIJN_API_KEY = "62bfe84194efe62a3b19036b"

import requests
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_eur_to_usd_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
    response = requests.get(url) # GET REQUEST

    if response.status_code == 200:
        data = response.json()

        if "USD" in data["conversion_rates"]:
            return data["conversion_rates"]["USD"]
        else:
            console.print("Fout: USD wisselkoers niet gevonden.")
            return None
    else:
        console.print(f"Fout: {response.status_code} - {response.text}")
        return None
def convert_eur_to_usd(amount, exchange_rate):
    return amount * exchange_rate

def main():
    api_key = MIJN_API_KEY

    eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
    console.print()
    exchange_rate = get_eur_to_usd_rate(api_key)

    if exchange_rate is None:
        console.print("[red]Wisselkoers kon niet worden opgehaald.[/red]")
        return

    usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)
    resultaat = (
        f"[red]{eur_amount}[/red] EUR is gelijk aan "
        f"[green]{usd_amount:.2f}[/green] USD\n"
        f"(Wisselkoers: 1 EUR = {exchange_rate} USD)"
    )

    console.print(
Panel(
            resultaat,
                title="[bold yellow]Berekening wisselkoers[/bold yellow]",
                border_style="yellow",
                width=60
            ),
            justify="center"
    )

response = requests.get(
    f"https://v6.exchangerate-api.com/v6/{MIJN_API_KEY}/codes"
)

print(response.status_code)
print(response.text)

main()
"""
#BONUS











