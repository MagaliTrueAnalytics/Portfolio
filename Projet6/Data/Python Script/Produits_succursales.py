#webscrapping de weedcrawler pour extraire les produits des succursales selon les IDs
import requests
from bs4 import BeautifulSoup
import csv
import time

categories_cibles = ["Fleurs Séchées", "Haschich", "Moulu", "Préroulés"]
headers = {"User-Agent": "Mozilla/5.0"}

def extraire_produits_succursale(succursale_id, succursale_nom):
    url = f"https://quebec.weedcrawler.ca/store/{succursale_id}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    produits = []
    h2_tags = soup.find_all("h2")

    for h2 in h2_tags:
        categorie = h2.get_text(strip=True)
        if categorie not in categories_cibles:
            continue

        table = h2.find_next("table")
        if not table:
            continue

        rows = table.find_all("tr")[1:]  # Skip header
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                marque_nom = cols[0].get_text(strip=True)
                type_produit = cols[1].get_text(strip=True)
                produits.append({
                    "Succursale": succursale_nom,
                    "ID": succursale_id,
                    "Catégorie": categorie,
                    "Marque - Nom": marque_nom,
                    "Type": type_produit
                })

    return produits

# Lecture des succursales
ids_succursales = []
with open("ids_succursales.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ids_succursales.append({
            "Nom": row["Nom"],
            "ID": int(row["ID"])
        })

# Scraping global
tous_produits = []
for succ in ids_succursales:
    print(f"Traitement de : {succ['Nom']} ({succ['ID']})")
    produits = extraire_produits_succursale(succ["ID"], succ["Nom"])
    tous_produits.extend(produits)
    time.sleep(1)

# Sauvegarde
with open("produits_succursales_cibles.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Succursale", "ID", "Catégorie", "Marque - Nom", "Type"])
    writer.writeheader()
    writer.writerows(tous_produits)

print("✅ Extraction terminée avec succès.")

