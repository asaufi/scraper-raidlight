# Raidlight Scraper – Test Technique

## Étape 1 : Extraction des liens produits d’une page
Dans un premier temps, le script charge **une seule catégorie** (exemple : vêtements femme) et extrait les liens produits (`/products/...`) grâce à BeautifulSoup.  
Cette étape a permis de valider la logique d’extraction.

---

## Étape 2 : Parcours de plusieurs catégories
Ensuite, j’ai élargi le script pour **parcourir plusieurs catégories du site** en une seule exécution.  
J’ai défini une liste d’URLs correspondant à différentes sections du site (`femme`, `homme`, `accessoires`, `sacs`) et j’ai ajouté une boucle qui :

1. Charge chaque page de catégorie.
2. Extrait les liens produits de chacune.
3. Concatène tous les résultats dans une liste commune.

### Exemple d’utilisation
```bash
python scraper.py
