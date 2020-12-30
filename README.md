# Mini_Projet_Lotka_Volterra_Gr218
Github mini projet modélisation 1A CS 2020-2021 : Lotka_Volterra groupe 218 
Lien du github : https://github.com/TanguyColleville/Mini_Projet_Lotka_Volterra_Gr218

# Auteurs : 
Matthieu Briet 
Antoine Pagneux 
Tanguy Colleville 

# Structure 
Un dossier dev qui contient les codes de simulations
Un dossier rapport latex qui contient notre fichier pdf, qui est notre rapport ainsi que tous les fichiers nécessaire à la création de ce dernier. 
Un fichier requirement.txt qui regroupe l'ensemble des packages nécessaire au lancement et bon fonctionnement de notre modèle. 
Un fichier readme.md qui vient en aide à l'utilisateur de ce projet. 

# Rapport 

Le rapport pdf se trouve dans le dossier rapport_latex, il vous suffit d'ouvrir l'unique fichier pdf qui se trouve dans ce dossier. 


# Pour lancer le programme

Il vous suffit de 

Dans le terminal, se placer dans le repertoire du projet
cd Python/repDuProjet (si on est à la racine)

Création d’environnement virtuel
Python -m venv [NOM VENV]

Activer l’environnement
source [NOM VENV]/bin/activate si MACOS
Si Windows 
cd [NOM VENV] puis Scripts\Activate.bat 

En demeurant dans [NOM VENV] taper pip install -r requirements.txt

Vous êtes à présent de en mesure d'utiliser notre modèle.
# Le programme 

Ouvrir le programme et le lancer en veillant à sélectionner votre environnement virtuel comme interpreteur. 
Les graphiques vont s'ouvrir un à un. Il suffit de fermer un graphique pour que le suivant s'affiche.
Vous pouvez à présent jouir de la liberté d'ajuster les différents paramètres du modèle, en sachant que chaque paramètre bénéficie d'une explication détaillée dans l'annexe de ce projet.
Attention, pour simuler l'abscence de sardine au début il ne suffit pas de mettre la population initiale à 0 d'autres paramètres sont à régler conformément aux explications données en annexe.

# Conclusion 
On peut dire que nos résultats en termes d'analyse temporelle corresponde à nos attendes. La littérature nous également permis de déterminer les valeurs des paramètres dans le système de Lotka Volterra afin de modéliser l'évolution des populations de sardines et de requins dans la mer Adriatique. Plus de détail dans notre rapport PDF. 

# Références
https://www.scipy.org/
https://numpy.org/
http://ipython.org/
https://matplotlib.org/
http://www.banquept.fr/documents/2014/MementoPythonScilab.pdf

