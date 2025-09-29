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

## Étape 3 : Passage à Selenium pour le contenu dynamique

En testant l’extraction des prix avec **BeautifulSoup uniquement**, je me suis rendu compte que certaines informations (prix actuel, promotions, disponibilité) n’étaient pas présentes dans le HTML statique renvoyé par `requests`.  
En réalité, le site charge une partie du contenu **de manière dynamique via JavaScript**, ce qui empêche BeautifulSoup de les voir directement.  

Pour résoudre ce problème, j’ai intégré **Selenium** afin de simuler un vrai navigateur. Selenium exécute le JavaScript de la page et permet ainsi de :

1. Charger les pages produits dans un navigateur contrôlé par Python.  
2. Attendre le rendu complet des éléments dynamiques (comme le prix affiché).  
3. Extraire ensuite le HTML final et continuer le parsing avec BeautifulSoup.  

### Exemple de sortie pour un produit
```json
{
  "url": "https://raidlight.com/products/maillot-de-trail-femme-r-light",
  "titre": "R-LIGHTMaillot de trail manches courtes femme",
  "prix": "€49,92 EUR",
  "description": "UN T-SHIRT DE TRAIL RESPIRANT Conçu pour le trail running léger, le t-shirt R-light pèse 100 grammes et est l'un des t-shirts les plus légers de notre collection. Il possède des micro-trous sous les bras et un col demi-zip qui facilite la régulation de la température de votre corps. Enfin, le polyester recyclé à 80% est une matière très respirante."
}


