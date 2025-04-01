import create_database 
import sqlite3
import del_database
import random
import fonctions_jeu
#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()

co = sqlite3.connect("TeacherdleDB.db") #recuperation du connecteur
cu = co.cursor() #recuperation du curseur

create_database.initialisation_table(co,cu)# on initialise la table avec ces deux éléments

#fin de la mise en place, on commence le jeu
a = random.randint(1, 2)    #choix d un id de professeur aléatoire
objectif = cu.execute("SELECT nom from Teachers WHERE id={}".format(a)) 
print(cu)
nom_objectif = objectif.fetchall()   #on récupère le nom du professeur "cible" et on le montre pour l'instant
PROF_RECHERCHE = nom_objectif[0]
print(PROF_RECHERCHE[0])
tableau_recherche_not_fetched = cu.execute("SELECT * from Teachers WHERE id={}".format(a))
tableau_recherche = tableau_recherche_not_fetched.fetchall()
win = 0
nbr_essais = 5
while win !=1 and nbr_essais != 0:
    nbr_essais = nbr_essais-1
    guess = input()
    print(PROF_RECHERCHE[0])
    print(guess)
    if PROF_RECHERCHE[0] == guess:
        print("win")
        break
    else: 
        result_guess_not_fetched = cu.execute("SELECT * from Teachers WHERE nom ='{}' ".format(guess))
        result_guess = result_guess_not_fetched.fetchall()
        print(result_guess)
        for i in range (8):
            if (result_guess[0])[i] == (tableau_recherche[0])[i]:
                print("vrai")
            else :
                print("faux")
        print(" fin des infos, on peut re guess")