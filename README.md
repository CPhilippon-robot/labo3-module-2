# Laboratoire 3 - Module 2 (étape 2)
## La logique booléenne - Jeu Guess Who ?

### Date de remise : vendredi 1er novembre, 16h05

## Attentes de ce laboratoire :
0. Créer une copie de GuessWho_ORIGIN.py et la renommer avec votre nom (par exemple : GuessWho_CORINNE)
1. Remplir la documentation demandée (documentation.txt)
2. Compléter le niveau bronze, argent ou or
3. S'assurer que le programme fonctionne

*******
Dans ce laboratoire, vous mettrez en pratique la création de structure logique (if-else-elif) et la formulation de conditions.

Votre but est d'améliorer le programme proposé pour une version simplifiée du Jeu "Guess Who". Vous ne pouvez l'améliorer qu'avec des structures logiques simples (if-else-elif).

En tant qu'élève, vous pouvez choisir le niveau d'amélioration que vous souhaitez faire.

Les améliorations demandées/proposées sont les suivantes : 

__Niveau bronze__ : Vous devez rendre toutes les questions "stupid proof" pour au moins une tentative. Voir l'exemple aux lignes 72-75 

__Niveau argent__ : S'assurer de rendre les questions logiques à l'aide d'une séquence de if-else-elif, et ainsi permettre au programme d'en diminuer le nombre demandé selon les réponses de l'utilisateur. Bref, optimiser le jeu. Ne pas modifier les questions ou leur nature, seulement optimiser l'ordre en fonction des réponses reçues par l'utilisateur. 

(Par exemple, dans ce jeu, une femme ne peut pas avoir de moustache ou être chauve. Il y a peut-être aussi d'autres impossibilités ou façons de déduire plus rapidement des informations, à vous de les trouver !)

__Niveau or__ : Faire en sorte que la première question posée soit déterminée de manière aléatoire.  

Voir https://www.w3schools.com/python/module_random.asp au besoin

--------------------------------------
## Ressources
https://docs.google.com/spreadsheets/d/1LoF-IJ1IVnmD7E6jm3s2qZQ6jHsF5iD_1Wm-gFJQupA/edit?usp=sharing 

--------------------------------------

## Fonctionnement du programme :
Lignes 1 à 67 : Nous définissons les constantes et les listes nécessaires. 

Lignes 4 à 27 : Chaque personnage est une liste CONSTANTE contenant ses attributs.

Ligne 29 : Nous créons une liste contenant chaque personnage (donc, une liste de liste)

Ligne 30 : Nous créons une liste avec le nom des personnages, en chaîne de caractères.

Ligne 32 : Nous créons un dictionnaire qui associera chaque personnage à une valeur booléenne (vrai ou faux)

Lignes 59 à 66 : Nous créons les questions dans des constantes, question d'alléger le code

Ligne 90 : Nous créons une liste qui contiendra les réponses

Lignes 93 à 100 : Comparaison entre notre liste de réponse et les listes constantes, puis changement dans le dicitonnaire (nous y reviendrons après la relâche) pour ensuite afficher le résultat

Lignes 102 à 115 : Nous demandons à l'utilisateur de confirmer

*******
_Sources et références_

