from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse

BASE_URL = "https://raidlight.com"


def get_soup(url):
    options = Options()
    options.add_argument("--headless")  # ne pas ouvrir de fenêtre
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)  # attendre que JS s’exécute
    html = driver.page_source
    driver.quit()

    return BeautifulSoup(html, "html.parser")

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

def extrait_infos_produit(url):
    """Récupère les informations principales d'un produit depuis sa page."""
    soup = get_soup(url)

    # Exemple : à adapter selon la structure HTML réelle du site
    titre = soup.find("div", {"class": "product__title"})
    titre = titre.get_text(strip=True) if titre else "N/A"

    prix_span = soup.select_one("span.price-item--last span.money") \
            or soup.select_one("span.price-item--regular span.money")

    prix = prix_span.get_text(strip=True) if prix_span else "N/A"



    description = soup.find("div", {"class": "description-details"})
    description = description.get_text(strip=True) if description else "N/A"

    return {
        "url": url,
        "titre": titre,
        "prix": prix,
        "description": description
    }

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

    print("\n=== Extraction des informations détaillées ===")
    produits_details = []
    
    urls_uniques = list(set(tous_les_produits))

    for lien in urls_uniques[:100]:  # limite à 100 produits max
        print(f"Analyse de {lien}")
        infos = extrait_infos_produit(lien)
        produits_details.append(infos)
        time.sleep(1)  # pause pour rester poli avec le site

    # Exemple d’affichage
    for p in produits_details[:5]:  # juste un aperçu
        print(p)

    print(f"\nTotal produits analysés : {len(produits_details)}")
