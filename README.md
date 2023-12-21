# Wines Reviews
Etudiants :
- Clément Brigliano
- David Crevoiserat
- Jihad Falfoul

Ce travail présente une application de visualisation de données liées du domaine du vin à destination d'amateurs de vin. 

# Installation
1. Cloner le projet : `git clone https://github.com/clecleBriBri/Wine_Review_EDA.git`
2. Créer un environnement virtuel : `python -m venv .venv`
3. Activer l'environnement virtuel :
- Windows : `.venv\Scripts\activate`
- Linux : `source .venv/bin/activate`
4. Installer les dépendances : `pip install -r requirements.txt`
5. Lancer l'application : `python app.py`
6. Attendre l'apparition du message suivant : `Running on http://127.0.0.1:8050`
7. Ouvrir le lien (`http://127.0.0.1:8050`) dans un navigateur web

# Documentation
## Choix des données
Le dataset a été trouvé sur Kaggle : https://www.kaggle.com/datasets/zynicide/wine-reviews/. Il est issu du site internet [WineEnthusiast](https://www.wineenthusiast.com/) et contient différentes données sur des vins du monde entier (note, critique, prix, région, etc.).

## Intention, message à transmettre et public
Le but de ce projet est de proposer des visualisations permettant de guider un amateur de vin dans son choix de vin. Il pourra ainsi explorer les données de façon intuitive et trouver efficacement le vin qui lui convient en fonction de ses critères (prix, note, provenance, etc.).

## Représentation
Ce chapitre présente les différentes visualisations proposées dans l'application et les choix qui ont été faits pour les réaliser.

### Informations générales
- Nous avons choisi d'utiliser des couleurs adaptées au daltonisme issu de la palette de Paul Tol.
- Nous avons ajouté du storytelling pour guider l'utilisateur dans l'application et permettre une meilleure compréhension des données et des visualisations.
- Tous les graphiques sont interactifs (zoom, survol, filtrage). Nous avons choisi d'ajouter ces fonctionnalités afin de répondre au mantra "Overview first, zoom and filter, then details-on-demand."

### Qualité et production des vins par pays
Ce graphique utilise une représentation sous forme de carte du monde. Nous avons choisi cette représentation car la nature des données (pays) s'y prête bien. 
Les données représentées sont modifiables via des boutons. L'utilisateur peut ainsi choisir de visualiser la qualité des vins par pays ou la production de vin par pays.
Dans les deux cas, les pays sont colorés en fonction de la valeur de la donnée. Les pays ayant une valeur élevée sont colorés en vert et les pays ayant une valeur faible sont colorés en rouge. 
Nous avons choisi d'utiliser ces couleurs précises car elles sont intuitives pour l'utilisateur. En effet, le vert est souvent associé à une valeur bonne ou élevée et le rouge à une valeur mauvaise ou faible.

L'objectif de cette visualisation est d'introduire le sujet en proposant à l'utilisateur de comprendre quels sont les pays qui produisent le plus de vin et de quelle qualité sont les vins produits par ces pays.

### Distribution de la qualité par rapport à la quantité
Ce graphique utilise une représentation sous forme de nuage de points. Nous avons choisi cette représentation car elle permet de visualiser la répartition des données de façon intuitive et, dans le cas d'une corrélation entre les données, de la mettre en évidence aisément. Une liste déroulante permet de modifier les données représentées. L'utilisateur peut ainsi choisir de visualiser la qualité par rapport à la quantité dans le monde ou par continent. De plus, un second filtre permet à l'utilisateur de choisir d'isoler ou de retirer certains pays de la visualisation.

L'objectif de cette visualisation est de montrer à l'utilisateur si un pays qui produit beaucoup devrait être privilégié par rapport à un pays qui produit peu (ou inversement).

### Mots les plus fréquents dans les critiques positives
Ce graphique utilise une représentation sous forme d'histogramme horizontal afin de représenter les 10 mots les plus fréquents dans les critiques positives (plus de 90 points). Nous avons choisi cette représentation et non pas un wordcloud car nous trouvons que ce dernier est moins lisible et moins intuitif. Une liste déroulante permet de modifier les données représentées en choisissant le continent d'origine des vins.

L'objectif de cette visualisation est de permettre à l'utilisateur de choisir un vin en fonction des mots qui reviennent le plus souvent dans les critiques positives. Par exemple, si l'utilisateur souhaite acheter un vin européen, il saura que si le mot "fruit" apparaît dans une critique, il y a de fortes chances que le vin soit bon.

### Pourcentage de chance qu'un vin appartienne à une catégorie en fonction de son prix
Ce graphique utilise une représentation sous forme d'histogramme à barres empilées. Nous avons choisi cette représentation car la nature des données (deux pourcentages par catégorie) s'y prête bien. Pour chaque catégorie de vin, deux barres sont représentées. La première représente le pourcentage de chance qu'un vin coutant moins d'un certain prix appartienne à cette catégorie. La seconde représente le pourcentage de chance qu'un vin coutant plus d'un certain prix appartienne à cette catégorie. Un champ texte permet à l'utilisateur de modifier la limite de prix.

Cette visualisation à deux objectifs :
- Montrer à l'utilisateur que, de façon générale, le prix d'un vin est un indicateur de sa catégorie.
- Permettre à l'utilisateur de "prédire" la catégorie d'un vin en fonction de la quantité d'argent qu'il souhaite dépenser.

### Points obtenus en fonction du nombre de variétés produites
Ce graphique utilise une représentation sous forme de nuage de points. Nous avons choisi cette représentation car comme expliqué précédemment, elle permet de rapidement détecter une corrélations entre les données si elle existe

L'objectif de cette visualisation est de montrer à l'utilisateur que le nombre de variétés produites par un vigneron n'est pas un indicateur de la qualité de ses vins.

## Critique des outils utilisés
- Dash : très pratique car permet d'intégrer des visualisations Plotly dans une application web rapidement et d'ajouter un niveau d'interactions supplémentaires via des inputs (sliders, champ texte, etc.) qui ne sont pas disponibles dans Plotly de base.