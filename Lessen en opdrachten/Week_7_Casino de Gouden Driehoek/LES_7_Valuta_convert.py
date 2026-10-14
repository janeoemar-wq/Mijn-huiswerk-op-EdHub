"""
Stappenplan
0 IMPORTS+RICH+CONSOLE+API KEY(Haal alle ondersteunde valuta op)
1 bronvaluta kiezen (EUR)
2 doelvaluta kiezen (USD)
3 bedrag invoeren
4 wisselkoers ophalen
5 resultaat tonen
"""

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

MIJN_API_KEY = "62bfe84194efe62a3b19036b"

console = Console()

#hier haalt de api met mijn API-Key de ondersteunde valuta
def toon_valuta(data, start):
    table = Table(
        border_style="bright_yellow",
        show_header=False
    )

    codes = []

    for code, naam in data["supported_codes"]:
        codes.append(f"{code} - {naam}")

    pagina = codes[start:start + 30]

    for a in range(10):
        kolom1 = pagina[a] if a < len(pagina) else ""
        kolom2 = pagina[a + 10] if a + 10 < len(pagina) else ""
        kolom3 = pagina[a + 20] if a + 20 < len(pagina) else ""

        table.add_row(kolom1, kolom2, kolom3)

    console.print(
        Panel(
            table,
            title="Ondersteunde valuta: Code | Land | Munteenheid",
            border_style="bright_yellow",
            width=120
        )
    )


def haal_geldige_valuta_op():
    url = f"https://v6.exchangerate-api.com/v6/{MIJN_API_KEY}/codes"
    #Antwoord van mijn request is, vertaald in jason taal:
    response = requests.get(url)
    data = response.json()
    # ik wil alle valutanamen die ik van json krijg in een table met 3 kolommen
    toon_valuta(data, 0)

#STAP 2 lijst met gedlige valuta
    geldige_valuta = []

    for code, naam in data["supported_codes"]:
        geldige_valuta.append(code)
    return geldige_valuta, data
geldige_valuta, data = haal_geldige_valuta_op()

start = 0

van_bron_valuta = input(
    "VAN welk munteenheid wil je de geld omzetten?\n"
    "Voer een 3-letterige valutacode in of typ 'MEER': "
).strip().upper()
console.print()
#STAP 3

while van_bron_valuta not in geldige_valuta:
    if van_bron_valuta == "MEER":
        start += 30
        toon_valuta(data, start)
    else:
        console.print("Ongeldige invoer!", style="red")
    van_bron_valuta = input(
        "Voer een 3-letterige valutacode in of typ 'MEER': ").strip().upper()
naar_doel_valuta = input(
    "NAAR welk munteenheid wil je de geld omzetten?\n"
    "Voer een 3-letterige valutacode in of typ 'MEER': "
        ).strip().upper()
while naar_doel_valuta not in geldige_valuta and naar_doel_valuta != "MEER":
    console.print("Ongeldige valutacode!", style="red")
    naar_doel_valuta = input(
        "Voer een 3-letterige valutacode in of typ 'MEER': "
        ).strip().upper()

bedrag = float(input(f"Hoeveel {van_bron_valuta} wil je omrekenen? "))
console.print(f"Gekozen bron valuta: [bold blue]{van_bron_valuta}[/bold blue]")
console.print(f"Gekozen doel valuta: [bold green]{naar_doel_valuta}[/bold green]")

url = (
    f"https://v6.exchangerate-api.com/v6/{MIJN_API_KEY}"
    f"/pair/{van_bron_valuta}/{naar_doel_valuta}/{bedrag}"
)

response = requests.get(url)
data = response.json()

resultaat = data["conversion_result"]
#STAP 5
console.print(
    Panel(
        f"{bedrag:.2f} {van_bron_valuta}       =       {resultaat:.2f} {naar_doel_valuta}",
        title="Valuta Converter",
        border_style="bright_yellow",
        width=50
    )
)
