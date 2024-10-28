### AUCUNE MODIFICATION NÉCESSAIRE JUSQU'À LA LIGNE 67 ###
import random

ALEX = ("H", "N", "Br", "N", "N", "P", "O", "N")
ALFRED = ("H", "R", "Bl", "N", "N", "P", "O", "N")
ANITA = ("F", "J", "Bl", "N", "N", "P", "N", "N")
ANNE = ("F", "N", "Br", "N", "N", "G", "N", "N")
BERNARD = ("H", "Br", "Br", "O", "N", "G", "N", "N")
BILL = ("H", "R", "Br", "N", "N", "P", "N", "O")
CHARLES = ("H", "J", "Br", "N", "N", "P", "O", "N")
CLAIRE = ("F", "R", "Br", "O", "O", "P", "N", "N")
DAVID = ("H", "J", "Br", "N", "N", "P", "N", "N")
ERIC = ("H", "J", "Br", "O", "N", "P", "N", "N")
FRANS = ("H", "R", "Br", "N", "N", "P", "N", "N")
GEORGE = ("H", "Bl", "Br", "O", "N", "P", "N", "N")
HERMAN = ("H", "R", "Br", "N", "N", "G", "N", "O")
JOE = ("H", "J", "Br", "N", "O", "P", "N", "N")
MARIA = ("F", "Br", "Br", "O", "N", "P", "N", "N")
MAX = ("H", "N", "Br", "N", "N", "G", "N", "N")
PAUL = ("H", "Bl", "Br", "N", "O", "P", "N", "N")
PETER = ("H", "Bl", "Bl", "N", "N", "G", "N", "N")
PHILIP = ("H", "N", "Br", "N", "N", "P", "N", "N")
RICHARD = ("H", "Br", "Br", "N", "N", "P", "O", "O")
ROBERT = ("H", "Br", "Bl", "N", "N", "G", "N", "N")
SAM = ("H", "Bl", "Br", "N", "O", "P", "N", "O")
SUSAN = ("F", "Bl", "Br", "N", "N", "P", "N", "N")
TOM = ("H", "N", "Bl", "N", "O", "P", "N", "O")

LISTE_VALEUR_PERSO = [ALEX, ALFRED, ANITA, ANNE, BERNARD, BILL, CHARLES, CLAIRE, DAVID, ERIC, FRANS, GEORGE, HERMAN, JOE, MARIA, MAX, PAUL, PETER, PHILIP, RICHARD, ROBERT, SAM, SUSAN, TOM]
LISTE_NOM_STRING_PERSO = ["Alex", "Alfred", "Anita", "Anne", "Bernard", "Bill", "Charles", "Claire", "David", "Eric", "Frans", "George", "Herman", "Joe", "Maria", "Max", "Paul", "Peter", "Philip", "Richard", "Robert", "Sam", "Susan", "Tom"]

dictionnaireEtatPerso = {
ALEX : True,
ALFRED : True,
ANITA : True,
ANNE : True,
BERNARD : True,
BILL : True,
CHARLES : True,
CLAIRE : True,
DAVID : True,
ERIC : True,
FRANS : True,
GEORGE : True,
HERMAN : True,
JOE : True,
MARIA : True,
MAX : True,
PAUL : True,
PETER : True,
PHILIP : True,
RICHARD : True,
ROBERT : True, 
SAM : True, 
SUSAN : True,
TOM : True
}

QUESTION1 = "Votre personnage est-il un homme (H) ou une femme (F) ?"
QUESTION2 = "Votre personnage a-t-il les cheveux Noir (N), Roux (R), Jaune (J), Brun (Br) ou Blanc (Bl) ?"
QUESTION3 = "Votre personnage a-t-il les yeux Bruns (Br) ou Bleus (Bl) ?"
QUESTION4 = "Votre personnage porte-t-il un chapeau ? (O ou N)"
QUESTION5 = "Votre personnage porte-t-il des lunettes ? (O ou N)"
QUESTION6 = "Votre personnage a-t-il un petit (P) ou un gros (G) nez ?"
QUESTION7 = "Votre personnage a-t-il une moustache ? (O ou N)"
QUESTION8 = "Votre personnage est-t-il chauve ? (O ou N)"

### LES MODIFICATIONS NÉCESSAIRES SE FONT À PARTIR D'ICI ###

reponse1 = str(input(QUESTION1))

if reponse1 == "H" or reponse1 == "F": # Exemple pour niveau bronze
    reponse1 = reponse1
else:
    reponse1 = str(input(QUESTION1 + ". Répondez correctement cette-fois ci !"))

reponse2 = str(input(QUESTION2))



reponse3 = str(input(QUESTION3))
reponse4 = str(input(QUESTION4))
reponse5 = str(input(QUESTION5))
reponse6 = str(input(QUESTION6))
reponse7 = str(input(QUESTION7))
reponse8 = str(input(QUESTION8))

### AUCUNE MODIFICATION NÉCESSAIRE APRÈS CETTE LIGNE ###

listeDeReponse = tuple([reponse1, reponse2, reponse3, reponse4, reponse5, reponse6, reponse7, reponse8])


for i in range(len(LISTE_VALEUR_PERSO)): # Pour chaque élément [i] de la liste LISTE_VALEUR_PERSO
    for j in range(len(listeDeReponse)): # Pour chaque élément [j] de notre liste de réponse
        if LISTE_VALEUR_PERSO[i] != listeDeReponse: # Si la valeur dans la liste à la position [i] n'est pas égale à notre liste de réponse
            dictionnaireEtatPerso[LISTE_VALEUR_PERSO[i]] = False # Assigner la valeur False à la position [i] dans le dictionnaire de personnage

for k in range(len(LISTE_VALEUR_PERSO)): # Pour chaque élément [k] de la liste LISTE_VALEUR_PERSO
    if dictionnaireEtatPerso[LISTE_VALEUR_PERSO[k]] == True: # Si la valeur dans liste à la position [k] est vrai
        print("Le nom de votre personnage est-il " + LISTE_NOM_STRING_PERSO[k] + " ?") # Imprimer dans le terminal 
       
verification = str(input("Confirmez avec O ou N :"))

if verification == "O":
    print("Super, j'ai gagné !")
elif verification == "N":
     print("Vous êtes certain ? Avez-vous bien rempli les réponses ? J'ai toujours raison !")
else:
    print("Répondez par O ou N seulement SVP !")
    verification = str(input("Confirmez avec O ou N :"))

if verification == "O":
    print("Super, j'ai gagné !")
elif verification == "N":
     print("Vous êtes certain ? Avez-vous bien rempli les réponses ? J'ai toujours raison !")




