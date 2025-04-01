import create_database 
import sqlite3
import del_database
import random
#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()

co = sqlite3.connect("TeacherdleDB.db") #recuperation du connecteur
cu = co.cursor() #recuperation du curseur

create_database.initialisation_table(co,cu)# on initialise la table avec ces deux éléments

#fin de la mise en place, on commence le jeu
a = random.randint(1, 2)    #choix d un id de professeur aléatoire
objectif = cu.execute("SELECT nom from Teachers WHERE id={}".format(a)) 
nom_objectif = objectif.fetchall()   #on récupère le nom du professeur "cible" et on le montre pour l'instant
b = nom_objectif[0]
print(b[0])
    
win = 0
nbr_essais = 5
#while win !=1 or nbr_essais != 0:
    #nbr_essais -= 1
    #algorithme de jeu
    