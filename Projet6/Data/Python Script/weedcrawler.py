#webscrapper weedcrawler.ca pour extraire les noms de succursales et dates d'ouverture
import requests
from bs4 import BeautifulSoup
import csv

url = "https://quebec.weedcrawler.ca/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Repérer la table principale
rows = soup.find_all("tr")[1:]  # On saute l'en-tête

succursales = []
for row in rows:
    cols = row.find_all(["th", "td"])
    if len(cols) >= 3:
        nom = cols[0].get_text(strip=True)
        date_ouverture = cols[1].get_text(strip=True)
        date_update = cols[2].get_text(strip=True)
        succursales.append({
            "Nom": nom,
            "Ouverte le": date_ouverture            
        })

# Écriture dans un fichier CSV
with open("succursales.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Nom", "Ouverte le"])
    writer.writeheader()
    writer.writerows(succursales)

print("Les données ont été enregistrées dans 'succursales.csv'.")
