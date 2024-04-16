
# J'importe le module 'requests' de la bibliothèque 'requests'.
# Ce module permet d'envoyer des requêtes HTTP/1.1 avec Python.
# Il est très pratique pour interagir avec des API ou pour faire du web scraping.
import requests

# J'importe la classe 'BeautifulSoup' depuis le module 'bs4' de la bibliothèque 'BeautifulSoup'.
# BeautifulSoup est un outil formidable pour analyser des documents HTML et XML.
# Il fournit des méthodes pour naviguer dans la structure du document et en extraire des données.
from bs4 import BeautifulSoup

# Je définis l'URL du site Allociné contenant les informations sur les films.
# Cette URL est la porte d'entrée pour accéder aux données qui seront analysées et extraites.
url = "https://www.allocine.fr/film/"

# Je crée une fonction pour vérifier si l'URL est accessible.
# Cela permet de prévenir l'utilisateur si le site est hors ligne ou si l'URL est erronée.
def verifier_url(url):
    # J'envoie une requête GET à l'URL et je récupère la réponse HTTP grâce à 'requests.get'.
    # Cette requête simule une visite sur le site web comme le ferait un navigateur.
    response = requests.get(url)
    
    # J'examine le code de statut HTTP retourné pour évaluer le résultat de la requête.
    # Un code de statut de 200 indique que tout s'est bien passé.
    if response.status_code == 200:
        print("OK - La page a été chargée avec succès.")
    elif response.status_code == 400:
        print("400 Bad Request - La requête n'a pas pu être traitée à cause d'une syntaxe erronée.")
    else:
        # Si le code de statut n'est ni 200 ni 400, je signale que l'URL est bloquée ou inaccessible.
        print("URL bloquée ou inaccessible pour une autre raison.")

# J'appelle la fonction 'verifier_url' pour tester l'accessibilité de l'URL avant de poursuivre.
verifier_url(url)

# Je récupère le contenu HTML de la page pour analyse.
response = requests.get(url)

# J'analyse le contenu HTML récupéré pour naviguer dans la structure du document.
soup = BeautifulSoup(response.text, 'html.parser')

# Je veux sélectionner les éléments qui contiennent les vignettes des films.
# J'ai trouvé que les images des films sur Allociné ont une classe 'thumbnail-img'.
film_elements = soup.select('img.thumbnail-img')

# Je veux extraire le nom des films depuis l'attribut 'alt' de ces images.
# L'attribut 'alt' contient le titre du film suivi de "Bande-annonce VF".
# J'utilise la méthode 'split' pour ne garder que le titre du film.
film_names = [img['alt'].split(" Bande-annonce")[0] for img in film_elements if " Bande-annonce" in img['alt']]

# Je veux afficher les noms des films extraits pour vérifier les résultats.
for name in film_names:
    print(name)

