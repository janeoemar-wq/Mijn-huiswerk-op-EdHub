# Euro/Dollar koers applicatie
Je gaat een euro/dollar converter bouwen in python. 
Je gaat gebruik maken van de “requests” library en de gratis exchangerate-api
Uiteindelijk wil je een output krijgen als: 
Voer het bedrag in EUR in: 32 
32.0 EUR is gelijk aan 35.11 USD (Wisselkoers: 1 EUR = 1.0973 USD)
## Stappenplan: 
Stap 1,2 en 4 zijn voorbereidingen. In stap 4 maak je de methode die de API aanroept en de 
wisselkoers ophaalt. In stap 5 maak je de methode die de 
## Opzet
1: Vraag een gratis api-key aan door je te registreren op https://www.exchangerateapi.com/
2: Maak een nieuw python bestand aan in PyCharm
3: Importeer de “requests” library (denk ook aan pip)
## API functie
4: Maak een functie met een parameter die de koers ophaalt vanuit de API: 
def get_eur_to_usd_rate(api_key):
Hierin gaan we de huidige koers ophalen vanaf de API. 
4.1: Maak een url variabele met de url: 
f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
4.2: Gebruik de requests librarie om een GET request te doen naar de url. Sla de uitkomst 
op een een variabel “response”
4.3: Maak een if-statement die checkt of de status juist is met 
response.status_code == 200
Of
response.ok
4.4: In de else print je een foutmelding: 
print(f"Fout: {response.status_code} - {response.text}")
return None
4.5: Haal de json uit de response met de .json() methode. Sla dit op in een variabele “data”
4.6: Maak een (nested) if-statement die checkt of “USD” in de “conversion_rates” van de 
json zit: 
if "USD" in data["conversion_rates"]:
 return data["conversion_rates"]["USD"]
else:
 print("Fout: USD wisselkoers niet gevonden.")
 return None
Je kunt ook eerst eens "print(data)” doen om te zien dat wat daar allemaal in zit. Onder 
andere een “conversion_rates” dict met daar in onder andere een “USD” waarde.
## Covert functie
5: Maak een methode “convert_eur_to_usd” die 2 parameters ontvangt, “amount” en 
“exchange_rate”. In de body van deze methode return je amount * return_rate
return amount * exchange_rate
## Main functie
6: Maak de main methode (zonder parameters) en vergeet deze ook niet aan te roepen op 
het eind van het script, anders gebeurt er niks als je de applicatie opstart.
6.1: Definieer een “api-key” variabele in je main methode waar je jou api key in opslaat. 
6.2: Maak een “eur_amount” variabele waatin je met “input” de gebruiker om een bedrag 
vraagt
eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
6.3: Gebruik de get_eur_to_usd_rate methode om de huidige wisselkoers op te halen:
exchange_rate = get_eur_to_usd_rate(api_key)
6.4: Gebruik de conver_eur_to_usd methode om het ingevoerde bedrag naar dollars om te 
zetten: 
usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)
6.5: Print de output:
print(f"{eur_amount} EUR is gelijk aan {usd_amount:.2f} USD 
(Wisselkoers: 1 EUR = {exchange_rate} USD)")
## Bonus
Maak een algemene currency converter. Nu kan de gebruiker alleen EUR naar USD 
vertalen. Zorg dat de gebruiker zelf kan kiezen welke valuta hij/zij gaat vertalen (mits deze 
door de API ondersteund wordt natuurlijk