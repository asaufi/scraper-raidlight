# Raidlight Scraper – Test Technique

## Étape 1 : Extraction des liens produits

Dans cette première phase, j’ai écrit un script en **Python** qui :
- Charge une page du site [raidlight.com](https://raidlight.com).
- Analyse le contenu HTML avec **BeautifulSoup**.
- Parcourt toutes les balises `<a>` et filtre celles qui contiennent `/products/` dans leur `href`.
- Recompose les URLs absolues grâce à `urllib.parse.urljoin`.
- Affiche en sortie la liste des liens produits trouvés sur la page.

### Exemple d’utilisation
```bash
python scraper.py
