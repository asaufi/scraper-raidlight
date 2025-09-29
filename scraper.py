import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

BASE_URL = "https://raidlight.com"

def get_soup(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def extrait_liens_produits_depuis_page(soup):
    """Donne les liens <a> des produits dans une page (catalogue ou catégorie)."""
    liens = []
    # Example : si les liens produits ont une classe “product-card__link” (à vérifier sur le site)
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Filtrer les liens produits — heuristique : contiennent “/products/” dans l’URL
        if "/products/" in href:
            liens.append(urllib.parse.urljoin(BASE_URL, href))
    return liens


if __name__ == "__main__":
        # Étape 2 : parcourir plusieurs catégories
    categories = [
        "https://raidlight.com/pages/vetement-femme",
        "https://raidlight.com/pages/vetement-de-trail-homme",
        "https://raidlight.com/collections/fin-de-series",
        "https://raidlight.com/pages/trail-to-be-alive"
    ]

    tous_les_produits = []

    for url_cat in categories:
        print(f"\n🔎 Chargement de {url_cat}")
        soup = get_soup(url_cat)
        produits = extrait_liens_produits_depuis_page(soup)
        tous_les_produits.extend(produits)

    print("\n=== Liens produits trouvés sur toutes les catégories ===")
    for lien in tous_les_produits:
        print(lien)
    print(f"\nTotal produits collectés : {len(tous_les_produits)}")

