#webscrapper weedcrawler.ca pour extraire les noms et IDs des succursales 
import requests
from bs4 import BeautifulSoup
import re
import csv

url = "https://quebec.weedcrawler.ca/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

succursales = []

# Chaque ligne de la table contient un lien vers la succursale
for row in soup.find_all("tr")[1:]:  # On saute l'en-tête
    link = row.find("a", href=True)
    if link and "/store/" in link["href"]:
        nom = link.get_text(strip=True)
        match = re.search(r"/store/(\d+)", link["href"])
        if match:
            succursale_id = int(match.group(1))
            succursales.append({
                "Nom": nom,
                "ID": succursale_id
            })

# Sauvegarde dans un CSV
with open("ids_succursales.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Nom", "ID"])
    writer.writeheader()
    writer.writerows(succursales)

print("Les identifiants des succursales ont été enregistrés dans 'ids_succursales.csv'.")
