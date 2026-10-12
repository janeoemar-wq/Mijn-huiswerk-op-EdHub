"""
pip install requests geinstalleerd in terminal
import requests
"""

import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
json = response.json()
print(json["value"])

url = 'https://api.example.com/data'
params = {'search': 'keyword', 'page': 2}

response = requests.get(url, params=params)
url = 'https://api.example.com/data?search=keyword&page=2'
response = requests.get(url

