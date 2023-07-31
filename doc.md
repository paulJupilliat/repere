# Fonctionnement de Django


## Repere
- L'application :
    - elle contient les fichiers de settings neccessaire au reférencement des repertoires utilisés afin de les renseignés et d'en prendre compte. Elle permet aussi d'ajouter le traitement d'image dans ce cas la de l'application
<br>
- Urls :
    - Fichier permettant de reférencer les différents urls utilisé et ainsi leur donner un nom, un chemin, et une fonction qui fait office de liason entre ce modele et la view.
<br> 
<br>

## Les stores

- elle comptient des fichiers de template permettant l'affichage, un fichier models.py qui reférencie les classes de ce store ( store contient les classes des articles )
<br>
- view.py : 
    - Ce fichier est présent dans chaque store créer, il permet de communiquer avec Repere et son fichier urls en contenant les fonctions appelees dans urls.py
    - Ces différentes fonction prennent en parametre la requete mais auss c'est possible que le slug soit présent. Le slug s'assure de l'unicité de l'article (dans notre cas) et permet ainsi de créer un url a partir de lui car il ne contient pas d'espace etc.
    Ces fonctions ont pour role de retourner une page html avec un context qui est souvent une requete sql. Grace a ce contexte, la page html a la capacité de parcourir par exemple les articles du panier.
    <br> en dehors des fonctions simple qui fournissent de la bd au HTML on a aussi la création de fonctions utiles pour le code html commme par exemple le bouton "ajouter au panier" est relié a ce fichier et c'est ici qu'est gérer l'ajout du panier veritablement.


