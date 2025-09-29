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
    url_test = "https://raidlight.com/pages/vetement-femme"  # une catégorie au hasard
    print(f"Chargement de {url_test}")
    soup = get_soup(url_test)

    produits = extrait_liens_produits_depuis_page(soup)

    print("Liens produits trouvés sur cette page :")
    for lien in produits:
        print(lien)
